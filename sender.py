import json
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from persistence import get_previous_messages


def send_email(message_object, short_story):
    msg = MIMEMultipart()

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Word of the day ' + str(message_object['word_of_the_day']).upper()
    msg['From'] = "noreply@rommeldetorres.me"
    msg['To'] = "detorresrc@gmail.com"

    msg.attach(MIMEText(format_message(message_object), "html"))
    msg.attach(MIMEText("<hr/><h1 style='color: blue'>Short Story</h1>" + short_story, "html"))
    msg.attach(MIMEText("<hr/><h1 style='color: blue'>Previous Word of the Day</h1>" + format_prev_messages(), "html"))

    server = smtplib.SMTP(os.getenv('EMAIL_HOST'), int(os.getenv('EMAIL_PORT')))
    server.starttls()
    server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))

    try:
        server.send_message(msg)
        print("Sent!")
    except Exception as e:
        print(e)
    finally:
        server.quit()


def format_message(message_object):
    html = f"<h1>Word of the day <strong style='color: blue;'>{str(message_object['word_of_the_day']).upper()}</strong></h1>"
    html += "<br/><br/><strong>ENGLISH LANGUAGE: </strong><br/>"
    html += "<strong>Synonyms: </strong><br/><li>"
    html += "</li><li>".join(message_object['english']['synonyms'])
    html += "</li><strong>Sentences: </strong><br/><li>"
    html += "</li><li>".join(message_object['english']['sentences'])
    html += "</li><br/><br/><strong>TAGALOG LANGUAGE: </strong><br/>"
    html += "<strong>Synonyms: </strong><br/><li>"
    html += "</li><li>".join(message_object['tagalog']['synonyms'])
    html += "</li><strong>Sentences: </strong><br/><li>"
    html += "</li><li>".join(message_object['tagalog']['sentences'])
    html += "</li>"
    return html


def format_prev_messages():
    html_prev_messages = ""
    for message in get_previous_messages():
        message_object = json.loads(message)
        html_prev_messages += f"<br/><strong style='color: blue;'>{str(message_object['word_of_the_day']).upper()}</strong><br/><br/><strong>ENGLISH LANGUAGE: </strong><br/>"
        html_prev_messages += "<strong>Synonyms: </strong><br/><li>"
        html_prev_messages += "</li><li>".join(message_object['english']['synonyms'])
        html_prev_messages += "</li><strong>Sentences: </strong><br/><li>"
        html_prev_messages += "</li><li>".join(message_object['english']['sentences'])
        html_prev_messages += "</li><br/><br/><strong>TAGALOG LANGUAGE: </strong><br/>"
        html_prev_messages += "<strong>Synonyms: </strong><br/><li>"
        html_prev_messages += "</li><li>".join(message_object['tagalog']['synonyms'])
        html_prev_messages += "</li><strong>Sentences: </strong><br/><li>"
        html_prev_messages += "</li><li>".join(message_object['tagalog']['sentences'])
        html_prev_messages += "</li><hr/>"

    return html_prev_messages
