from django.conf import settings
from django.core.mail import EmailMessage
from django_cron import CronJobBase, Schedule


class EmailPhotoCronJob(CronJobBase):
    """
    Send an email with a Pi Camera photo.
    """
    # Run every 6 hours (when DEBUG is False)

    # TODO: Retrieve the interval and duration from database
    RUN_INTERVAL = 0 if settings.DEBUG else 360

    schedule = Schedule(run_every_mins=RUN_INTERVAL)
    code = 'cron.EmailPhotoCronJob'

    def do(self):
        job_timestamp = time.strftime('%D %H:%M:%S')
        message = 'PyGrow photo update at %s.' % job_timestamp

        # Create email message
        email = EmailMessage(
            # Subject
            '[PyGrow] Photo update',
            # Message
            message,
            # Sender
            'from@example.com',
            # Recipient
            ['to@example.com'],
        )

        # Attach file
        email.attach_file('/pygrow/photos/%s.png')

        # Send email
        email.send(fail_silently=False)
