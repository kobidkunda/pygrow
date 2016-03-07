from django.conf import settings
from django_common.helper import send_mail
from django_cron import CronJobBase, Schedule


class EmailAlertCronJob(CronJobBase):
    """
    Send an email with a Temperature or Humidity alert.
    """
    # Run every 6 hours (when DEBUG is False)
    RUN_INTERVAL = 0 if settings.DEBUG else 360

    schedule = Schedule(run_every_mins=RUN_INTERVAL)
    code = 'cron.EmailAlertCronJob'

    def do(self):
        job_timestamp = time.strftime('%D %H:%M:%S')
        message = 'PyGrow alert at %s.' % job_timestamp

        # Send email
        send_mail(
            # Subject
            '[PyGrow] Photo update',
            # Message
            message,
            # Sender
            'from@example.com',
            # Recipient
            ['to@example.com'],
            fail_silently=False
        )
