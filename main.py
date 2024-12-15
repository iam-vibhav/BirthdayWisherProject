import pandas as pd
import smtplib
import datetime as dt
import random
MY_EMAIL = "vibhavkadavakollu2005@gmail.com"
MY_PASSWORD = "ahcp qbkt ubjh jnvw"

class Birthday:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.birthday = None

    def is_birthday(self):
        today = dt.datetime.now().date()
        return today.month == self.birthday.month and today.day == self.birthday.day


birthday_details = pd.read_csv("birthdays.csv")
birthday_list = []

for _, row in birthday_details.iterrows():
    bday = Birthday()
    bday.name = row['name']
    bday.email = row['email']
    bday.birthday = dt.date(row['year'], row['month'], row['day'])
    birthday_list.append(bday)

letters_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

for bday in birthday_list:
    if bday.is_birthday():
        letter_path = random.choice(letters_list)
        with open(letter_path) as letter:
            contents = letter.read()
            new_contents = contents.replace("[NAME]", bday.name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=bday.email, msg=new_contents)
