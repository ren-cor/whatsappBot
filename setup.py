import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':

	load_dotenv()
	CHROME_SESSION = os.getenv("CHROME_SESSION")
	chrome_options = Options()
	chrome_options.add_argument("user-data-dir={chrome_session}".format(chrome_session=CHROME_SESSION))
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://web.whatsapp.com/")

	input("On the chrome browser that opened, scan the QR code to login into WA web, then press return here to close..")