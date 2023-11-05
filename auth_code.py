import urllib.parse

def get_authorization_url(client_id, redirect_uri, scope):
    base_url = 'https://accounts.spotify.com/authorize'
    query_params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': scope,
        'show_dialog': 'true',  # Forces the consent screen to be shown every time. This is useful for testing.
    }
    url = f"{base_url}?{urllib.parse.urlencode(query_params)}"
    return url

# Usage:
client_id = "6cffce53882c4c3494bc6e258fc44cb0"
client_secret = "4fb8c7af4b23477c9afa930fbfaaa6d6"
artist_id = "1Xyo4u8uXC1ZmMpatF05PJ"

redirect_uri = 'localhost://api'
scope = 'user-library-read'  # Space-separated string if multiple scopes
authorization_url = get_authorization_url(client_id, redirect_uri, scope)

print(authorization_url)
# Redirect the user to this UR