from django.conf import settings
from django.core.mail import EmailMessage
from django_cron import CronJobBase, Schedule
from monitoring.models import EmailAlert


class EmailAlertCronJob(CronJobBase):
    """
    Send an email with a Temperature or Humidity alert.
    """
    # Run every 6 hours (when DEBUG is False)
    RUN_INTERVAL = 0 if settings.DEBUG else 360

    schedule = Schedule(run_every_mins=RUN_INTERVAL)
    code = 'cron.EmailAlertCronJob'

    # Check EmailAlert model for value
    include_photo = True

    def do(self):
        job_timestamp = time.strftime('%D %H:%M:%S')
        message = 'PyGrow alert at %s.' % job_timestamp

        # Create email message
        email = EmailMessage(
            # Subject
            '[PyGrow] Alert',
            # Message
            message,
            # Sender
            'from@example.com',
            # Recipient
            ['to@example.com'],
        )

        if include_photo == True:
            # Attach file
            email.attach_file('/pygrow/photos/%s.png')

        # Save EmailAlert to database
        email_alert = EmailAlert()
        email_alert.timestamp = job_timestamp
        # email_alert.recipient = recipient
        email_alert.include_photo = include_photo
        # email_alert.min_temperature = min_temperature
        # email_alert.max_temperature = max_temperature
        # email_alert.min_humidity = min_humidity
        # email_alert.max_humidity = max_humidity
        email_alert.save()

        # Send email
        email.send(fail_silently=False)
