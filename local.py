from dotenv import load_dotenv
from openai import OpenAI

from common import get_ai_message
from sender import send_email
from persistence import add_new_word, get_words, initialize
import json

load_dotenv()
initialize()

def main():
    try:
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=get_ai_message(get_words()),
            stream=False
        )

        message = completion.choices[0].message.content.strip()
        message_object = json.loads(message)
        send_email(message_object)
        add_new_word(message_object['word_of_the_day'], message)

        return {
            'statusCode': 200,
            'body': json.dumps('Success')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }


main()
