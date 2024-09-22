from config import Config

class Commands():


	def __init__(self, sheet):

		self.commands = {
			"bill": self.bill,
			"expense": self.expense,
			"help":self.help,
			"info":self.info,
			"link":self.link,
			"ping": self.ping,
			"status": self.status,
			"kill": self.kill

		}

		self.sheet = sheet

	def bill(self, command):
		if not command:
			return {"status": "EXECUTED", "template":"billSyntax"}
		parts = command.split(".")

		# Check if correct number of params
		if len(parts) < Config.billsParams:
			return {"status": "ERROR", "error":"Unsufficient number of parameters"}
		if len(parts) > Config.billsParams + 1:
			return {"status": "ERROR", "error":"Too many parameters inserted"}

		# Who benefited from the payment
		if len(parts) == Config.billsParams + 1:
			additional_values = self.parseInitials(parts[Config.billsParams])
			values = parts[:Config.billsParams] + additional_values
		else: values = parts + ["X" for i in range(Config.numberParticipants)]
		values[Config.billsPayerIndex] = self.parsePayer(values[Config.billsPayerIndex])
		worksheet = Config.billsWorksheet
		self.sheet.appendRow(worksheet, values)
		return {"status": "EXECUTED", "template":"billSuccess"}

	def expense(self,command):
		if not command:
			return {"status": "EXECUTED", "template":"expenseSyntax"}
		parts = command.split(".")

		# Check if correct number of params
		if len(parts) < Config.expenseParams:
			return {"status": "ERROR", "error":"Unsufficient number of parameters"}
		if len(parts) > Config.expenseParams + 1:
			return {"status": "ERROR", "error":"Too many parameters inserted"}

		# Who benefited from the payment
		if len(parts) == Config.expenseParams + 1:
			additional_values = self.parseInitials(parts[Config.expenseParams])
			values = parts[:Config.expenseParams] + additional_values
		else: values = parts + ["X" for i in range(Config.numberParticipants)]
		values[Config.expensePayerIndex] = self.parsePayer(values[Config.expensePayerIndex])
		worksheet = Config.expenseWorksheet
		self.sheet.appendRow(worksheet, values)
		return {"status": "EXECUTED", "template":"expenseSuccess"}


	def help(self, command):
		return {"status": "EXECUTED", "template":"help"}

	def info(self, command):
		return {"status": "EXECUTED", "template":"info"}

	def kill(self, command):
		return {"status": "EXECUTED", "action":"KILL"}

	def link(self, command):
		return {"status": "EXECUTED", "template":"link"}

	def ping(self, command):
		return {"status": "EXECUTED", "template":"ping"}

	def status(self, command):
		statusRanges = Config.summaryRanges
		res = self.sheet.getStatus(statusRanges["worksheet"], statusRanges["namesRange"], statusRanges["dataRange"])

		return {"status": "EXECUTED", "template":"status", "data":res}

	def parseInitials(self, initials):
		#initialise list of flag for each person
		values = ["" for i in range(Config.numberParticipants)]
		for char in initials.upper():
			values[Config.initials[char][0]] = "X"
		return values

	def parsePayer(self, payer):
		payer = payer[0].upper()
		return Config.initials[payer][1]