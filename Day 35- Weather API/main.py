import requests
import smtplib

# Define variables
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "Your OpenWeatherMap API"
my_email = "Your e-mail"
password = "E-mail's password"
to_mail = "E-mail address to send"
message = "It's going to rain today. Remember to bring an umbrella"
subject = "Hey!"

# Define api parameters
weather_params = {
    "lat": 41.008240,
    "lon": 28.978359,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

# Get data
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()

hourly = data["hourly"]

# Check if it will rain in 12 hours
will_rain = False

for hour in hourly[:12]:
    if hour["weather"][0]["id"] < 700:
        will_rain = True
        break

# If it's going to rain send an email
if will_rain:
    # Connection to sending email service
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_mail,
                            msg=f"Subject:{subject}\n\n{message}")
