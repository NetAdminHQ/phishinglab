import imaplib
from config import EMAIL, PASSWORD, IMAP_SERVER, IMAP_PORT

def connect_imap():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    return mail

def fetch_unread_emails(mail):
    status, messages = mail.search(None, '(UNSEEN)')
    return messages[0].split()
