import smtplib


class NotificationManager:
    def __init__(self):

        self.my_email = "Your Email"
        self.password = "Your Email Password"
        self.to_mail = "E-mail address to send"

    # Connection to sending email service
    def send_email(self, message: str):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email,
                                to_addrs=self.to_mail,
                                msg=f"Subject:Price Update\n\n{message}")
