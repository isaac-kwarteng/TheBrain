from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import getCoordinates

# Initializing the file path of the CSV file
csvFilePath: str = "Stops.csv"

# Initializing arguments for webdriver
service = Service()
driver = webdriver.Chrome()
driver.get("https://ghanapostgps.com/map/")
searchBox = driver.find_element(By.ID, "addsearch")
coordinates = getCoordinates.GetCoordinates(csvFilePath).get_coordinates()
print(coordinates)
