The project is based on Python and Django

Make sure you do 'pip install -r requirements.txt' inside a virtuale environment

Admin Credentials:
username : dhruvarora
password: dillirox123

To log into admin panel : 127.0.0.1:8000/admin


To manage deals -> Admin -> Deals
To manage orders -> Admin -> Orders
To manage users -> Admin -> Users


Scripts inside products/jobs/daily are meant to be executed on daily basis
And can be executed by putting the command "python manage.py runjobs daily" in a crontab or cronjob for 10AM everyday

Crontab for 10AM Everyday command : '* 10 * * * python manage.py runjobs daily'