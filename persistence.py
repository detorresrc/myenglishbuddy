from datetime import datetime
import pymongo
import os

mongo_client = None
db = None
messages = None


def initialize():
    global mongo_client, db, messages
    mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
    db = mongo_client[os.getenv("MONGO_DB")]
    messages = db["messages"]


def add_new_word(word, content):
    messages.insert_one({"word": word.lower(), "content": content, "created_at": datetime.now()})


def get_words():
    message_list = []
    for message in messages.find({}):
        message_list.append(message['word'])

    return ",".join(message_list)


def get_previous_messages():
    return_messages = []
    for message in messages.find().sort("created_at", pymongo.DESCENDING).limit(8):
        return_messages.append(message['content'])
    return return_messages

