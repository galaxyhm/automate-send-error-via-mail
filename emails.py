#! /usr/bin/env python3 
import smtplib
from email.message import EmailMessage
from time import time
import os 
import mimetypes

def generate_email(sender :str , recipient :str, subject :str, body:str ="", attachment_path: str="") -> EmailMessage:
    """
    generate a email message.
    if attachment is none, not attach a file.
    """
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    if attachment_path != "":
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as at:
            msg.add_attachment(at.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=os.path.basename(attachment_path))
    return msg


def send_email(msg):
    with smtplib.SMTP() as s:
        s.send_message(msg)


