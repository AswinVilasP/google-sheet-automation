import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = 'your_spreadsheet_id'  # Replace with your actual spreadsheet ID
# example: SAMPLE_RANGE_NAME = 'Sheet1!A1:F' The range of cells to read from
RANGE_NAME = "<sheetname>!<sheetrange>"

# Path to the service account key file
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'keys.json')  # Path to your service account key file

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Authenticate using the service account
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def sheet_function(name, phone, email, job, message):
  try:
      # Build the service
      service = build('sheets', 'v4', credentials=creds)

      # Call the Sheets API to read data
      sheet = service.spreadsheets()

      # Example: Append new data to the spreadsheet
      data = [[name, phone, email, job, message]]
      request = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                                      range='Sheet1!A1',
                                      valueInputOption='RAW',
                                      body={'values': data}).execute()
      print(f'{request.get("updates").get("updatedCells")} cells appended.')
  except HttpError as err:
      print(err)


sheet_function('john', 1234567890, 'example@gmail.com', 'devops engineer', 'Hi all!!')
