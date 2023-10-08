from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options



def song_downloader(song_link):
 
    options = Options()
    options.binary_location = '/path/to/firefox'
    driver = webdriver.Firefox(options=options)

    URL = "https://spotifymate.com/"

    # If geckodriver is on your system PATH, you can initialize it simply with:
    # driver = webdriver.Firefox()

    # If it's not on your PATH, provide the direct path:
    # driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

    driver.get(URL)

    # Let the page load (can be adjusted as per internet speed or site's response time)
    time.sleep(5)

    # Assuming you're referring to the "Search for a track..." input field
    # If there are other input fields you want to automate, you'll need to adjust the element selector accordingly.
    search_field = driver.find_element_by_css_selector("input[id='url']")

    # Input text into the search field
    search_field.send_keys(song_link)

    # Submit the form
    search_field.send_keys(Keys.RETURN)

    # Let the page load the results
    time.sleep(5)

    # Close the browser
    driver.close()