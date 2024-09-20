# Read environmental variables
import os
from dotenv import load_dotenv
load_dotenv()
#Set DEBUG to False to hide debug logs
DEBUG_FLAG = os.getenv("DEBUG")

def consoleLog(*args, debug=False):
	global DEBUG_FLAG
	if not debug:
		print("[LOGGER]: ", *args)
	elif DEBUG_FLAG:
		print("[DEBUG]: ", *args)