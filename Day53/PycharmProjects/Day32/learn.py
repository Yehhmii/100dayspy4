# import smtplib

# my_email = ""
# password = ""
#
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.ehlo()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="",
#                         msg="Subject:Hello\n\nThis is the body of the email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
print(month)

# creating your datetime
d_o_b = dt.datetime(year=1999, month=3, day=22)
print(d_o_b)

