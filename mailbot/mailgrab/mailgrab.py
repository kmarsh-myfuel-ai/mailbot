import sys
from datetime import datetime, timedelta

# EMAIL
import imaplib
# import email
import os

def mailgrab():
    print("Grabbing email!", file=sys.stderr)
    mail = imaplib.IMAP4_SSL(os.environ.get("EMAIL_IMAP_SERVER"))
    mail.login(os.environ.get("EMAIL_ADDRESS"), os.environ.get("EMAIL_PASSWORD"))
    mail.select(os.environ.get("EMAIL_FOLDER"))
    
    # data is a potentially empty list of IMAP email ids as a byte string, e.g. b'79 80 81 82 83 84 85 86 87 88'
    now = datetime.now()
    delta = timedelta(days=-int(os.environ.get("EMAIL_SEARCH_DAYS")))
    since_time = now + delta
    search_criteria = f'(SINCE "{since_time.strftime("%d-%b-%Y")}")'
    status, data = mail.search(None, search_criteria)

    print(data[0], file=sys.stderr)
    # for item in data[0].split():
    #     print(item, file=sys.stderr)
    # f = open('kotchi.txt', 'wb')
    # f.write(data)
    # f.close    