import datetime
now=datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))




from datetime import date,timedelta
dt=date.today() - timedelta(5)
print("current date:",date.today())
print('5 days before current date:',dt)

