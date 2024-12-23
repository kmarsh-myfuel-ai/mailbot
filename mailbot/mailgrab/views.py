from django.http import HttpResponse
from django.template import loader

from .models import EmailBytes
from .mailgrab import mailgrab

def index(request):
    last_ten_emails = EmailBytes.objects.order_by("-mailbot_update_date")[:10]
    template = loader.get_template("index.html")
    context = {
        "last_ten_emails": last_ten_emails,
    }
    return HttpResponse(template.render(context, request))

def grab(request):
    mailgrab()
    template = loader.get_template("grab.html")
    return HttpResponse(template.render({}, request))
