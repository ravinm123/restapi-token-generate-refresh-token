import requests

#jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwNjk4NzYwLCJpYXQiOjE3MjA2OTg0NjAsImp0aSI6ImZmNzcwOGU5YWU1ODQ2YmJhMjNlYWE4MWUwM2U2Yzg1IiwidXNlcl9pZCI6Mn0.Jgt2MGWu8Q8mlvaibqhdmXunQUlnzVVoCORJHEXuSeY"

import requests

# Replace 'your_actual_jwt_here' with your actual JWT token string
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwNjk4NzYwLCJpYXQiOjE3MjA2OTg0NjAsImp0aSI6ImZmNzcwOGU5YWU1ODQ2YmJhMjNlYWE4MWUwM2U2Yzg1IiwidXNlcl9pZCI6Mn0.Jgt2MGWu8Q8mlvaibqhdmXunQUlnzVVoCORJHEXuSeY"

url = 'http://127.0.0.1:8000/api/profile/'
headers = {
    'Authorization': f'Bearer {jwt_token}',
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses

    data = response.json()
    print(data)  # Print parsed JSON data or process it further
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
