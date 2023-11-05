import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Define your Firefox WebDriver options
options = Options()
options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'  # Make sure this path is correct

# Initialize the WebDriver
driver = webdriver.Firefox(options=options)
URL = "https://spotisongdownloader.com/"

# Function to handle the processing of each track
def process_track(track_id):
    song_link = 'https://open.spotify.com/track/' + track_id
    driver.get(URL)
    time.sleep(10)  # Wait for the page to load
    search_field = driver.find_element(By.CSS_SELECTOR, "input[id='id_url']")
    search_field.send_keys(song_link)
    search_field.send_keys(Keys.RETURN)    
    time.sleep(10)  # Wait for the results to load
    download_button = driver.find_element(By.ID, "download_btn")
    download_button.click()
    time.sleep(10)
    download_button = driver.find_element(By.ID, "quality")
    download_button.click()


# Main program
try:
    url = 'http://127.0.0.1:8000/spotifier/track/all/'
    response = requests.get(url)

    if response.status_code == 200:
        tracks_data = response.json()
        for track in tracks_data:
            spotify_id = track.get('spotify_id')
            process_track(spotify_id)  # Process each track
    else:
        print(f"Failed to retrieve data: Status code {response.status_code}")
finally:
    driver.quit()  # Make sure to close the driver after all commands
