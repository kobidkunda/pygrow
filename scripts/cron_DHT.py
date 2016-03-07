import subprocess
from crontab import CronTab

# subprocess.call([
#     'python',
#     '/pygrow/monitoring/utilities/DHTTools.py'
# ])

# PyGrow user
cron = CronTab(user='pygrow')

# Run DHTTools.py script
auto_response_job = cron.new(command='python /pygrow/monitoring/utilities/DHTTools.py >> /var/log/pygrow_cron_dht 2>&1')

# Run every 5 minutes
auto_response_job.minute.every(5)

cron.write()
