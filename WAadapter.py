# Part of the WhatsAppBot project by Renato Corradini


# import dependencies
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def openChat(chrome_session, group_name, headless=False):
	'''
	given a string with the group name to open, it returns a selenium driver
	'''
	chrome_options = Options()
	chrome_options.add_argument("user-data-dir={chrome_session}".format(chrome_session=chrome_session))
	if headless:
		chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://web.whatsapp.com/")
	wait=WebDriverWait(driver,100)

	target = '"{group_name}"'.format(group_name=group_name)
	contact_path = '//span[contains(@title,'+ target + ')]'
	contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
	contact.click()
	return driver


def send_msg(driver, text, header="[BOT]: "):
	wait=WebDriverWait(driver,1000)
	message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
	message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
	#Splitting on new_lines to avoid sending ENTER and removing \t to avoid pressing TAB

	message_box.send_keys(header)
	for part in text.replace("\t", "").split("\n"):
		message_box.send_keys(part)
		ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
	message_box.send_keys(Keys.ENTER)
	return header + text
	#Keys.ENTER
