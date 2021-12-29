import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "Your username"
TOKEN = "Your token id"

# Create new user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# Create graph
graph_endpoint = f"  {pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graph1",
    "name": "Goals",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# Get date
date = datetime.datetime.now().date()
date = "".join(str(date).split("-"))

# Create pixel
create_pixel_endpoint = f"{graph_endpoint}/graph1"

create_pixel_params = {
    "date": date,
    "quantity": "4"
}

# response = requests.post(url=create_pixel_endpoint, json=create_pixel_params, headers=headers)

# Update a pixel
update_pixel_endpoint = f"{create_pixel_endpoint}/{date}"

update_params = {
    "quantity": "1"
}

# response = requests.delete(url=update_pixel_endpoint, headers=headers)
