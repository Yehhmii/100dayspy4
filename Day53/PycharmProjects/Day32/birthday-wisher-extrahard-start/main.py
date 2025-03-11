import csv
import smtplib
import datetime as dt
import random
import pandas

my_email = ""
password = ""

now = dt.datetime.now()
today = (now.month, now.day)

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        conn.ehlo()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                      msg=f"Subject: happy Birthday! \n\n {contents}")



