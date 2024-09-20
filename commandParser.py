from logger import consoleLog
from commands import Commands

class CommandParser(Commands):

	# __init__ inherited

	def parse(self, command):

		words = command.split()

		if words[0].startswith("/"):

			commandWord = words[0][1:]

			if commandWord in self.commands:

				commandFunction = self.commands[commandWord]

				arguments = command[len(words[0])+1:]
				res = commandFunction(arguments)
				consoleLog("RAN COMMAND {}".format(commandFunction.__name__))
				return res


			else: return {
				"status":"ERROR",
				"error":"Unrecognised command, use /help for guidance"
				}

		else: return {"status":"OK", "debug":"NO COMMAND ENTERED"}