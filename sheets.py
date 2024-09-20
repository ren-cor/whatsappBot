from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load env variables
import os
from dotenv import load_dotenv
load_dotenv()



class Sheet():

	def __init__(self, service_account, spreadsheetId):

		# Attributes
		self.service_account = service_account
		self.spreadsheetId = spreadsheetId

		# Initialise
		credentials = self.authenticate()
		self.ss = build('sheets', 'v4', credentials=credentials)


	def authenticate(self):
		return service_account.Credentials.from_service_account_file(
			filename=self.service_account)

	def appendRow(self, worksheet, values):
		num_columnns = len(values)
		last_column = chr(64 + num_columnns)

		range_to_get = "A1:{}".format(last_column)

		res = self.ss.spreadsheets().values().get(
			spreadsheetId = self.spreadsheetId,
			range=worksheet + range_to_get,
			).execute()

		next_row = len(res["values"]) + 1
		cell_range = "A{}:{}{}".format(next_row, last_column, next_row)

		value_range_body = {
			"majorDimension":"ROWS",
			"values":(values,)
		}

		self.ss.spreadsheets().values().update(
			spreadsheetId = self.spreadsheetId,
			valueInputOption="USER_ENTERED",
			range=worksheet + cell_range,
			body = value_range_body
			).execute()


	def getStatus(self, worksheet, names_range, data_range):

		names = self.ss.spreadsheets().values().get(
			spreadsheetId = self.spreadsheetId,
			range=worksheet + names_range,
			).execute()

		balance = self.ss.spreadsheets().values().get(
			spreadsheetId = self.spreadsheetId,
			range=worksheet + data_range,
			).execute()

		return {
			"names":names["values"][0],
			"balance":balance["values"][0]
		}