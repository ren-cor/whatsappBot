from logger import consoleLog
from commands import Commands

class CommandParser(Commands):

	
	def __init__(self, sheet, commandChar):

		self.commandChar = commandChar

		# __init__inherited from Commands class
		Commands.__init__(self, sheet)

	def parse(self, command):

		words = command.split()

		if words[0].startswith(self.commandChar):

			commandWord = words[0][len(self.commandChar):]

			if commandWord in self.commands:

				commandFunction = self.commands[commandWord]

				arguments = command[len(words[0])+1:]
				res = commandFunction(arguments)
				consoleLog("RAN COMMAND {}".format(commandFunction.__name__), debug=True)
				return res


			else: return {
				"status":"ERROR",
				"error":"Unrecognised command, please use /help for further guidance"
				}

		else: return {"status":"OK", "debug":"NO COMMAND ENTERED"}