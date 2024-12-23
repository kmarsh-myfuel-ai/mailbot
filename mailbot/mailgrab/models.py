from django.db import models

# (venv) ken@i15-3535:~/code/myfuelai_devops/html$ grep -A 1 '^Message-ID' ExampleDispatchNotificationOrder.eml 
# Message-ID:
#  <SJ0PR03MB6550CA41D95E4A322D572912A9002@SJ0PR03MB6550.namprd03.prod.outlook.com>
# (venv) ken@i15-3535:~/code/myfuelai_devops/html$ grep -m 1 '^From' ExampleDispatchNotificationOrder.eml 
# From: MyFuelDispatch <myfueldispatch@jetagefuel.com>

class EmailEML(models.Model):
    email_message_id = models.CharField(max_length=995)
    email_from = models.CharField(max_length=320)
    mailbot_recieve_date = models.DateTimeField('mailbot_recieve_date')
    mailbot_update_date = models.DateTimeField('mailbot_update_date', auto_now=True)
    # email_eml = models.TextField()
    