import os
import datetime as dt
import smtplib
import random


my_email = 'calcguru2020@gmail.com'

def send_email(name,email):
    
    directory = 'letter_templates'
    files = os.listdir(directory)

    template_chosen = random.choice(files)


    with open(os.path.join(directory,template_chosen)) as f:
        contents = f.read()


    letter= contents.replace('[NAME]',name)

    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=os.environ.get('PASSWORD'))
        connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"Subject: HAPPY BIRTHDAY!\n\n{letter}")







   


current_date = dt.datetime.now()
current_day,current_month = current_date.day,current_date.month

with open('birthdays.csv') as f:
    for line in f:
        name,email,year,month,day = line.split(',')

        if int(month) == current_month and int(day) == current_day:
            send_email(name,email)







