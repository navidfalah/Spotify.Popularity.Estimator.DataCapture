# first start the django then execute this 


import requests


url = 'http://localhost:8000/your-endpoint/'  # Replace with your actual endpoint

# Send a GET request to the Django server
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    print("Request was successful!")
    print("Response content:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")


