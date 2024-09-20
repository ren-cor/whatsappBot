import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from WAadapter import openChat, send_msg
from logger import consoleLog
from commandParser import CommandParser
from config import MessageTemplate, Config
from sheets import Sheet

# Load env variables
import os
from dotenv import load_dotenv
load_dotenv()
CHROME_SESSION = os.getenv("CHROME_SESSION")
GROUP_NAME = os.getenv("GROUP_NAME")
SERVICE_ACCOUNT = os.getenv("SERVICE_ACCOUNT")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
HEADLESS = os.getenv("HEADLESS").lower() in ["true", "t", "1"]


s = Sheet(SERVICE_ACCOUNT, SPREADSHEET_ID)

cmdParser = CommandParser(sheet=s)
msgTemplate = MessageTemplate()
header = Config.header
messages = ["init"]
# testing
driver = openChat(CHROME_SESSION, GROUP_NAME, HEADLESS)
for msg in driver.find_elements(By.CLASS_NAME, "_ao3e.selectable-text.copyable-text"):
	messages.append(msg.text)
consoleLog("Started listening on group: {}".format(GROUP_NAME))
# Greet the group chat
send_msg(driver, msgTemplate.templates["greeting"], header)
while True:
	try:
		time.sleep(5)
		all_messages = driver.find_elements(By.CLASS_NAME, "_ao3e.selectable-text.copyable-text")
		last_recorded_message = messages[-1]
		counter = len(all_messages) - 1
		while counter > 0:
			if all_messages[counter].text == last_recorded_message:
				break
			else: counter -= 1
		new_messages = all_messages[counter+1:]
		for msg in new_messages:
			print("NEW MESSAGE: ", msg.text)
			messages.append(msg.text)
			# ignore bot messages
			if not msg.text.startswith(header):
				res = cmdParser.parse(msg.text)
				consoleLog(res, debug=True)
				if "status" in res.keys() and res["status"] == "ERROR":
					send_msg(driver, res["error"], header)
				if "action" in res.keys():
					if res["action"] == "KILL":
						consoleLog("Exiting application by /kill")
						exit()
				if "template" in res.keys():
					if "data" in res.keys():
						getTemplate = getattr(msgTemplate, res["template"])
						to_send = getTemplate(res["data"])
					else: to_send = msgTemplate.templates[res["template"]]
					send_msg(driver, to_send, header)

	except Exception as e:
		exception = type(e).__name__
		send_msg(driver, "An unexpected error occured: "+exception, header)
