from django.db import models

class EmailBytes(models.Model):
    imap_uid = models.IntegerField()
    message_id = models.CharField(max_length=995)
    message_from = models.CharField(max_length=320)
    mailbot_recieve_date = models.DateTimeField('mailbot_recieve_date')
    mailbot_update_date = models.DateTimeField('mailbot_update_date', auto_now=True)
    message_bytes = models.TextField()

    