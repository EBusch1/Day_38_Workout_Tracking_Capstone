import requests

# Nutritionix API info
APP_ID = ''
API_KEY = ''

# Physical Characteristics
GENDER = 'male'
WEIGHT_KG = 86.2
HEIGHT_CM = 142.24
AGE = 25

# Request header
nutrix_header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

# API Parameters - only query is required
nutrix_params = {
    'query': input("Tell me what exercises you did: "),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

nutrix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# making request
log_exercise = requests.post(headers=nutrix_header, url=nutrix_endpoint, json=nutrix_params)
log_exercise.raise_for_status()

# getting request details
exercise_details = log_exercise.json()
print(exercise_details)
