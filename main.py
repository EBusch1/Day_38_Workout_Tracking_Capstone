import requests
import datetime

# Nutritionix API info


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

# nutrix parameters - only query is required
nutrix_params = {
    'query': input("Tell me what exercises you did: "),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

# endpoints
nutrix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/c03ff789ef50eb41a3778adf9d64f297/myWorkouts/workouts'

# making request
log_exercise = requests.post(headers=nutrix_header, url=nutrix_endpoint, json=nutrix_params)
log_exercise.raise_for_status()

# getting request details
exercise_details = log_exercise.json()
print(exercise_details)

now = datetime.datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for activity in exercise_details['exercises']:

    exercise = activity['user_input'].title()
    duration = activity['duration_min']
    calories = activity['nf_calories']


    # sheety parameters
    sheety_params = {
        'workout': {
            'date': today,
            'time': time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        }
    }

    update_sheet = requests.post(headers=HEADER_AUTH, url=sheety_endpoint, json=sheety_params)
    update_sheet.raise_for_status()
    print(update_sheet.json())

