# configuration file for the project
class Config():

	header = "[BOT]: "
	numberParticipants = 4
	billsWorksheet = "Bills!"
	billsParams = 5
	billsPayerIndex = 3
	expenseWorksheet = "MiscExpenses!"
	expenseParams = 4
	expensePayerIndex = 2
	initials = {
		"E":[0, "Edoardo"],
		"F":[1, "Federico"],
		"R":[2, "Renato"],
		"U":[3, "Umberto"]
	}
	summaryRanges = {
		"worksheet":"Summary!",
		"namesRange":"B1:E1",
		"dataRange":"B4:E4"
	}

class MessageTemplate():

	templates = {

	"billSuccess": "New bill entry correctly inserted",
	"billSyntax": """To insert a bill entry use /bill <DD/MM/YYYY>.<Type>.<Description>.<Payer>.<Amount>

	Optionally, if this bill is only paid by some users, enter a dot and their initials after the amount.
	e.g. bill for R and F only: /bill <DD/MM/YYYY>.<Type>.<Description>.<Payer>.<Amount>.RF
	""",

	"expenseSuccess": "New expense entry correctly inserted",
	"expenseSyntax": """To insert an expense entry use /expense <DD/MM/YYYY>.<Description>.<Payer>.<Amount>

	Optionally, if this expense is only paid by some users, enter a dot and their initials after the amount.
	e.g. expense for R and F only: /expense <DD/MM/YYYY>.<Description>.<Payer>.<Amount>.RF
	""",

	"greeting":"Hello, I am the WA helper and my goal is to help you keep track of your expenses, type /help for a list of commands",

	"help": """ Hello I am the WA bot, I am here to help you keep track of your bills and expenses as a group.
	Find below the list of commands:

	
	/bill - use this command to add a bill to the list
	/expense - Use this command to add an expense to the list
	/help - This will show this help message
	/info - will display an information message regarding the bot
	/kill - this will will kill the bot
	/link - this will paste in the chat the link to the spreadsheet
	/ping - use this to find our if the bot joined the chat
	/status - this will show the current balance of payments

	""",

	"link": """ This is the link to the live google sheet with all transactions: 
	https://docs.google.com/spreadsheets/d/1o0vay9Fb2kA6GuWfBPPG6ZuhFS7KQoiCSBt6EzETCg4/
	""",

	"ping": "Pong!",

	"status": """This is the current balance for the users:
	{data_table}"""
	}

	def status(self, data):
		"""
		returns message to be given for the status provided data comes as a dictionary {"names":[], "balance":[]}
		"""
		names = data["names"]
		balance = data["balance"]
		print(names, balance)
		data_table = ""
		for i in range(len(names)):
			data_table += (names[i] + ": " + balance[i] + "\n")

		return self.templates["status"].format(data_table=data_table)

