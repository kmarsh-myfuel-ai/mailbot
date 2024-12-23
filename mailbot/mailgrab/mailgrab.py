import email
import sys
from datetime import datetime, timedelta

# EMAIL
import imaplib
import os

def mailgrab():
    print("Grabbing email!", file=sys.stderr)
    mail = imaplib.IMAP4_SSL(os.environ.get("EMAIL_IMAP_SERVER"))
    mail.login(os.environ.get("EMAIL_ADDRESS"), os.environ.get("EMAIL_PASSWORD"))
    mail.select(os.environ.get("EMAIL_FOLDER"))
    
    now = datetime.now()
    delta = timedelta(days=-int(os.environ.get("EMAIL_SEARCH_DAYS")))
    since_time = now + delta
    search_criteria = f'(SINCE "{since_time.strftime("%d-%b-%Y")}")'
    
    # data is a potentially empty list of IMAP email ids as a byte string, e.g. b'79 80 81 82 83 84 85 86 87 88'
    status, data = mail.search(None, search_criteria)
            
    for imap_uid in data[0].split():
        result, whole_email = mail.fetch(imap_uid, '(RFC822)')
        message = email.message_from_bytes(whole_email[0][1])
        email_from, encoding = email.header.decode_header(message.get("From"))[0]
        email_message_id, encoding = email.header.decode_header(message.get("Message-ID"))[0]
    
        
    
