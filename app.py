from config import Config
import time
from selenium.webdriver.common.by import By
from WAadapter import openChat, send_msg
from logger import consoleLog
from commandParser import CommandParser
from config import MessageTemplate, Config
from sheets import Sheet


class App():

	def __init__(self):

		# First load variables from .env into self.local_variables
		self.__load_variables()

		lv = self.local_variables
		self.sheet = Sheet(lv["SERVICE_ACCOUNT"], lv["SPREADSHEET_ID"])
		self.driver = openChat(lv["CHROME_SESSION"], lv["GROUP_NAME"], lv["HEADLESS"])
		self.cmdParser = CommandParser(sheet=self.sheet, commandChar=Config.commandChar)
		



	# internal function to load variables from .env
	def __load_variables(self):
		import os
		from dotenv import load_dotenv
		load_dotenv()
		self.local_variables = Config.local_variables
		for var in self.local_variables.keys():
			if self.local_variables[var] == ".ENV-STRING":
				self.local_variables[var] = os.getenv(var)
			elif self.local_variables[var] == ".ENV-BOOL":
				self.local_variables[var] = os.getenv(var).lower() in ["true", "t", "1"]


	def start(self):
		last_message = self.get_messages()[-1].text
		consoleLog("Started listening on group: {}".format(self.local_variables["GROUP_NAME"]))
		# Greet the group chat
		if Config.greetingFlag: send_msg(self.driver, MessageTemplate.templates["greeting"], Config.header)
		self.main_loop(last_message)


	def main_loop(self, last_message):

		header = Config.header
		msgTemplate = MessageTemplate()

		while True:
			try:
				time.sleep(Config.pollingRate)
				all_messages = self.get_messages()
				counter = len(all_messages) - 1
				while counter > 0:
					if all_messages[counter].text == last_message:
						break
					else: counter -= 1
				new_messages = all_messages[counter+1:]
				for msg in new_messages:
					consoleLog("NEW MESSAGE: ", msg.text)
					last_message = msg.text
					# ignore bot messages
					if not msg.text.startswith(header):
						res = self.cmdParser.parse(msg.text)
						consoleLog(res, debug=True)
						if "status" in res.keys() and res["status"] == "ERROR":
							send_msg(self.driver, res["error"], header)
						if "action" in res.keys():
							if res["action"] == "KILL":
								consoleLog("Exiting application by /kill")
								exit()
						if "template" in res.keys():
							if "data" in res.keys():
								getTemplate = getattr(msgTemplate, res["template"])
								to_send = getTemplate(res["data"])
							else: to_send = msgTemplate.templates[res["template"]]
							send_msg(self.driver, to_send, header)

			except Exception as e:
				exception = type(e).__name__
				send_msg(self.driver, "An unexpected error occured: "+exception, Config.header)


	def get_messages(self):
		messages = self.driver.find_elements(By.CLASS_NAME, Config.messagesHTMLClass)
		return messages
