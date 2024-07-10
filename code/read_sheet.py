import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = 'your_spreadsheet_id'  # Replace with your actual spreadsheet ID
# example: SAMPLE_RANGE_NAME = 'Sheet1!A1:F' The range of cells to read from
RANGE_NAME = "<sheetname>!<sheetrange>"

# Path to the service account key file
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'keys.json')  # Path to your service account key file

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Authenticate using the service account
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def get_sheet_data():
    try:
        # Build the service
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME).execute()
        
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            print('Name, Phone, Email, Job, Message:')
            for row in values:
                # Print columns A to E, which correspond to indices 0 to 4
                print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}')

    except Exception as e:
        print(f'Error retrieving data: {e}')

# Call the function to get data
get_sheet_data()
