
import urllib.parse
import secrets
from constants import client_id

# Define the necessary variables

redirect_uri = 'http://127.0.0.1:8000'
state = secrets.token_urlsafe(16)  # Generates a random URL-safe text string, similar to generateRandomString(16)

# Scopes that you want the application to access
scope = 'user-library-read'

# Building the authorization URL
auth_url = 'https://accounts.spotify.com/authorize'
auth_query_parameters = {
    'response_type': 'token',
    'client_id': client_id,
    'scope': scope,
    'redirect_uri': redirect_uri,
    'state': state
}

# Encoding the query parameters and appending them to the base URL
auth_query_string = urllib.parse.urlencode(auth_query_parameters)
full_auth_url = f'{auth_url}?{auth_query_string}'

print("Navigate to the following URL to authorize:", full_auth_url)





# BQBo7MKzrqO9syT5n2-UyZy9OWDARG7H4acjF9nbgYlKYL6bmQKNQ-NuHvVaXGaJCA6lRbqaPGjBlXszVloKOwX8Gn3IafMnNfzD1Wux69-SPxrVUsvP1o7RnjCWV8Gev2_i0y5TCaj1TqCQAh2hEJ9DR4xV1Mv1mgfNsI3udSZNolGpq9jP1YmMZURwQxhqHTn3y9CeHBigeHt7A3eZ&token_type=Bearer&expires_in=3600&state=kIaeYG8bQESbb9YgSVM1aA
