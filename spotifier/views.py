# views.py

from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
import requests
from urllib.parse import urlencode


client_id = "6cffce53882c4c3494bc6e258fc44cb0"
client_secret = "4fb8c7af4b23477c9afa930fbfaaa6d6"
artist_id = "1Xyo4u8uXC1ZmMpatF05PJ"



# The view to redirect the user to the Spotify authorization page
def auth(request):
    # Define the parameters for the authorization URL
    params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': "http://127.0.0.1:8000/spotifier/callback/",
        'scope': 'user-library-read',
    }

    # Redirect the user to Spotify's authorization page
    return redirect(f'https://accounts.spotify.com/authorize?{urlencode(params)}')

# The view to handle the callback from Spotify
def spotify_callback(request):
    error = request.GET.get('error')
    code = request.GET.get('code')

    if error:
        return HttpResponse(f'Error received from Spotify: {error}', status=400)
    
    if code:
        # Exchange the code for an access token
        access_token = get_access_token_private(client_id, client_secret, code, request.build_absolute_uri(reverse('spotify_callback')))
        
        # Use the access token to make authenticated requests to the Spotify API
        # ...
        headers = {
            "Authorization": f"Bearer {access_token}"
            }
        response = requests.get(f"https://api.spotify.com/v1/me/tracks", headers=headers)
        print(response.json())

        return HttpResponse('Authorization successful!')

    return HttpResponse('No code provided by Spotify.', status=400)

# The function to exchange the authorization code for an access token
def get_access_token_private(client_id, client_secret, code, redirect_uri):
    # Spotify's token endpoint
    token_url = 'https://accounts.spotify.com/api/token'
    
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
    }

    # Make a POST request to the token URL to exchange the code for an access token
    response = requests.post(token_url, auth=(client_id, client_secret), data=payload)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        # Handle error appropriately
        response.raise_for_status()

# urls.py
