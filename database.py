from datetime import datetime
import pymongo
import os

mongo_client = None
db = None
messages = None
recipients = None


def initialize():
    global mongo_client, db, messages, recipients
    mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
    db = mongo_client[os.getenv("MONGO_DB")]
    messages = db["messages"]
    recipients = db["recipients"]


def add_new_word(word, content, short_story):
    messages.insert_one({"word": word.lower(), "content": content, "short_story": short_story, "created_at": datetime.now()})


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


def get_recipients():
    list_recipients = []
    for recipient in recipients.find():
        list_recipients.append(recipient['email'])
    return list_recipients
