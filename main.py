import requests

# response = requests.get('https://api.agify.io?name=harry')
# body = response.json()

# print(body)


name = input('Your name: ')

age_response = requests.get(f'https://api.agify.io?name={name}')
age = age_response.json()['age']

gender_response = requests.get(f'https://api.genderize.io?name={name}')
gender = gender_response.json()['gender']

nationality_response = requests.get(f'https://api.nationalize.io/?name={name}')
nationality = nationality_response.json()['country'][0]['country_id']

print(f'You are probably a {age} years old {gender} from {nationality}.')
