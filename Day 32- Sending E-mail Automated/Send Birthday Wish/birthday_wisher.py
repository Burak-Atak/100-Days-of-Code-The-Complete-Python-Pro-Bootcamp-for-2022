from os import listdir
import random
import datetime as dt

my_email = "Your e-mail"
password = "E-mail's password"
to_mail = "E-mail address to send"

# Opens birthdays.csv file and read
with open("birthdays.csv") as text:
    text = text.readlines()

    # Its looks through every line and chose name, month, mail, day
    for i in text[1:]:
        new_text = i.split(",")
        name = new_text[0]
        month = new_text[3]
        mail = new_text[1]
        day = new_text[-1]
        current_month = dt.datetime.now().month
        current_day = dt.datetime.now().day

        # Check if chosen month and day equal current month and day
        if int(month) == int(current_month) and int(day) == int(current_day):
            import smtplib

            # List all files in letter_temples folder and randomly chose one of them
            files = listdir("letter_templates")
            chosen_text = random.choice(files)

            # Open chosen file and organise message
            with open(f"letter_templates/{chosen_text}") as message:
                message = message.read()
                new_message = message.replace("[NAME]", name.title())

                # Connection to sending email service
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=to_mail,
                                        # "Happy Birthday" is subject of mail
                                        msg=f"Subject:Happy Birthday\n\n{new_message}")