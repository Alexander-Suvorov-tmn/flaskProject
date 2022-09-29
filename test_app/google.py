from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from googleapiclient.discovery import build


# подключаеимся к google
CREDENTIALS_FILE = 'test_app/creds.json'
spreadsheet_id = '1O_NkvV7nfA1dxexgQBIMUxlCl1Ogr4-mbDZFR_p7FlE'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive']
)
httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http=httpAuth)
