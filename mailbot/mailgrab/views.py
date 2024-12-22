import sys
from django.http import HttpResponse
from django.template import loader

# EMAIL
import imaplib
import email
import os

from .models import EmailEML

def index(request):
    last_ten_emails = EmailEML.objects.order_by("-mailbot_update_date")[:10]
    template = loader.get_template("index.html")
    context = {
        "last_ten_emails": last_ten_emails,
    }
    return HttpResponse(template.render(context, request))

def grab(request):
    mailgrab()
    template = loader.get_template("grab.html")
    return HttpResponse(template.render({}, request))

def mailgrab():
    print("Grabbing email!", file=sys.stderr)
    mail = imaplib.IMAP4_SSL(os.environ.get("EMAIL_IMAP_SERVER"))
    mail.login(os.environ.get("EMAIL_ADDRESS"), os.environ.get("EMAIL_PASSWORD"))
    mail.select(os.environ.get("EMAIL_FOLDER"))
    
    status, data = mail.search(None, '(SINCE "20-Dec-2024")')

    for item in data:
        print(item, file=sys.stderr)
    # f = open('kotchi.txt', 'wb')
    # f.write(data)
    # f.close    