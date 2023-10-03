from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Specify the path to the GeckoDriver
driver_path = "path_to_your_geckodriver.exe"

# Use the Service object to initiate the driver
s = Service(driver_path)
browser = webdriver.Firefox(service=s)

# Navigate to Spotify's website
browser.get("https://www.spotify.com/")

# ... Rest of your code ...

# Don't forget to close the browser once done!
# browser.quit()
