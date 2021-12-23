import random
import smtplib

my_email = "Your e-mail"
password = "E-mail's password"
to_mail = "E-mail address to send"

# Opens quotes.txt and chose randomly one quote
with open("quotes.txt") as text:
    text_read = text.readlines()
    message = random.choice(text_read)

# Connection to sending email service
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_mail,
                        msg=f"Subject:-Type Subject Here-\n\n-type your message here-")
