from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

path =  "C:\Drivers\chromedriver_win32\chromedriver.exe"   # path of your chromedriver file
website = "https://web.whatsapp.com/"
phone_number =9095017512 # Write a phone number here
#photo_path = "C:\Users\Krishna\Downloads\13505.JPG"

# paste the path of the photo you want to send here


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.maximize_window()
time.sleep(30)  # scan QR code (we don't need to wait that much when we open existing browser)
