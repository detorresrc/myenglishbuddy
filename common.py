def get_ai_message(existing_words):
    return [
        {"role": "system", "content": "You are a helpful english teacher and developer assistant."},
        {"role": "user",
         "content": "Send word of the day, don't include the " + existing_words + ", with english and tagalog "
                                                                                  "synonyms, sample english and"
                                                                                  "tagalog sentences at least 3. Send "
                                                                                  "in a json format only,"
                                                                                  "Sample object {word_of_the_day: "
                                                                                  "'', english: {'synonyms': [], "
                                                                                  "'sentences':[]}, "
                                                                                  "tagalog: 'synonyms': [], "
                                                                                  "'sentences':[]}"
         }
    ]


def get_ai_short_story_message(word_of_the_day):
    return [
        {"role": "system", "content": "You are a helpful english teacher and web developer assistant."},
        {"role": "user", "content": f"Create a short story uses the word {word_of_the_day} , send in a html format only and make the '{word_of_the_day}' bold."}
    ]


def get_ai_format_email(message_object):
    return [
        {"role": "system", "content": "You are a helpful application developer assistant."},
        {"role": "user",
         "content": "format this in a html format, this is the json object: " + message_object
         }
    ]

