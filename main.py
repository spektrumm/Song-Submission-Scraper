# import gspread required libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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


# define a function to step through the rows in the sheet based off of the acquired start value from the save file
def stepThroughSheet(worksheet, lengthCount, aList, rowStart):
    i = rowStart + 1
    if rowStart < lengthCount:
        enumIndex = lengthCount - rowStart
        for n in range(enumIndex):
            rowVal = worksheet.row_values(i)
            splitVal = rowVal[2].split(',')
            for value in range(len(splitVal)):
                noSpaceStr = splitVal[value].replace(' ', '')
                aList.append(noSpaceStr)
            i += 1
    elif rowStart > lengthCount:
        print(
            f'Index out of range error, rowStart is = {rowStart}, and lengthCount is = {lengthCount}')
    else:
        print("rowStart indexing value is equal to the length; no new values have been added to the sheet.")


stepThroughSheet(ws, rawRowCount, strList, 1)
print(strList)


def listSort(strList):
    i = 0
    for submissions in strList:
        tempVal = strList[i]
        print(f' the current indexed item is = {tempVal}')
        if 'youtu.be' in str(tempVal) or 'youtube' in str(tempVal):
            ytList.append(tempVal)
        elif 'spotify' in str(tempVal):
            spotList.append(tempVal)
        else:
            appList.append(tempVal)
        i += 1


listSort(strList)
print(f'youtube list = {ytList}')
print(f'spotify list = {spotList}')
