import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 41.028015
MY_LNG = 28.678798
MY_EMAIL = "Your e-mail"
PASSWORD = "E-mail's password"
TO_MAIL = "E-mail address to send"


# Checks is iss is overhead
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data_iss = response.json()

    longitude = float(data_iss["iss_position"]["longitude"])
    latitude = float(data_iss["iss_position"]["latitude"])

    if MY_LAT - 5 < latitude < MY_LAT + 5 and MY_LNG - 5 < longitude < MY_LNG + 5:
        return True


# Checks is night
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response_2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_2.raise_for_status()

    data = response_2.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset < time_now < sunrise:
        return True


# If iss is overhead and it is night program will send you an email
while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TO_MAIL,
                                msg=f"Subject:Look up\n\nAnd see the iss")
    time.sleep(60)
