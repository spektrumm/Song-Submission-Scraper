# import gspread required libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import functions as fn

# GSPREAD SHEET DATA GENERAL
# define the scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'googleCredsKey.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Cobs Song Submission - Responses')

# get the first sheet of the Spreadsheet
ws = sheet.get_worksheet(0)
rawRowCount = len(ws.get_all_values())

# -- END GOOGLE API SETUP -- #

ytList = []
spotList = []
appList = []


strList = []
startNum = 0


def getRowStart(filename):
    with open(filename, 'r') as saveFile:
        startNum = saveFile.readline()

# getRowStart(save.txt)


fn.stepThroughSheet(ws, rawRowCount, strList, 1)
print(strList)

fn.listSort(strList, ytList, spotList, appList)
print(f'youtube list = {ytList}')
print(f'spotify list = {spotList}')
