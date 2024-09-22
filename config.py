# configuration file for the project
class Config():

	# To decide every how often the bot reads new messages from the chat, in seconds
	pollingRate = 3

	#The character that dictates commands
	commandChar  = "/"

	#Whether to send the greeting messsage in chat when the app starts
	greetingFlag = True

	# This will be at the start of every message sent by the bot
	header = "[BOT]: "
	

	billsWorksheet = "Bills!"
	billsParams = 5
	billsPayerIndex = 3
	expenseWorksheet = "MiscExpenses!"
	expenseParams = 4
	expensePayerIndex = 2

	# To configure the members of the group, in this dictionary add the initial as key, 
	# and the list [index, name] as object
	initials = {
		"E":[0, "Edoardo"],
		"F":[1, "Federico"],
		"R":[2, "Renato"],
		"U":[3, "Umberto"]
	}

	# Configure the place in the spreadsheet where the total balance for everyone is,
	# remember the ! at the end of the worksheet name
	summaryRanges = {
		"worksheet":"Summary!",
		"namesRange":"B1:E1",
		"dataRange":"B4:E4"
	}

	local_variables = {
		"DEBUG":".ENV-STRING",
		"GROUP_NAME":".ENV-STRING",
		"CHROME_SESSION":".ENV-STRING",
		"HEADLESS":".ENV-BOOL",
		"SERVICE_ACCOUNT":".ENV-STRING",
		"SPREADSHEET_ID":".ENV-STRING",

	}

	# If WA web changes the class name, update it here
	messagesHTMLClass = "_ao3e.selectable-text.copyable-text"

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
	Find the list of available commands below:

	
	/bill - use this command to add a bill to the list
	/expense - Use this command to add an expense to the list
	/help - This will show this help message
	/info - will display an information message regarding the bot
	/kill - this will will kill the bot
	/link - this will paste in the chat the link to the spreadsheet
	/ping - use this to find our if the bot joined the chat
	/status - this will show the current balance of payments

	""",

	"info": """ This WhatsApp bot is coded by RC. Version: 0.1""",

	"link": """ This is the link to the live google sheet with all transactions: 
	https://docs.google.com/spreadsheets/d/{spreadsheet_id}/
	""",

	"ping": "Pong!",

	"status": """Find the current balance for all users below:
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


	def link(self, data):
		return self.templates["link"].format(spreadsheet_id=data["SPREADSHEET_ID"])

