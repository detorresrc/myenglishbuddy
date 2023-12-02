from common import get_ai_short_story_message
from persistence import get_words


def generate_short_story(client, word_of_the_day):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=get_ai_short_story_message(word_of_the_day),
        stream=False
    )
    return completion.choices[0].message.content.strip()
