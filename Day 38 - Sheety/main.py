import requests
from datetime import datetime

# Define variables
APP_ID = "Your api id from nutritionix"
APP_KEY = "Your api key from nutritionix"
GENDER = "male"
WEIGHT = 84
HEIGHT = 184
AGE = 25

user_input = input("What exercise did you do today?:")

# Get user input data from nutritionix
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

response = requests.post(url=exercise_endpoint, json=exercise_params,  headers=HEADERS)
result = response.json()

# Determine calories, duration and exercise kind
exercise_kind = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

# Get date
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Access to your google sheets with using sheety api
sheety = "https://api.sheety.co/ec72731e11d8f46edff38609f3e5e81a/myWorkout/workouts"

sheety_params = {
  "workout": {
      "date": today_date,
      "time": now_time,
      "exercise": exercise_kind.title(),
      "duration": duration,
      "calories": calories,
    }
}

response = requests.post(url=sheety, json=sheety_params)
response.raise_for_status()
