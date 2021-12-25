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


def stepThroughSheet(worksheet, lengthCount, aList, rowStart):
    i = rowStart + 1
    #nsList = []
    if rowStart < lengthCount:
        enumIndex = lengthCount - rowStart
        for n in range(enumIndex):
            rowVal = worksheet.row_values(i)
            splitVal = rowVal[2].split(',')
            for value in range(len(splitVal)):
                noSpaceStr = splitVal[value].replace(' ', '')
                aList.append(noSpaceStr)
                # print(aList)  # debug

            i += 1
        # return(spotList)
    elif rowStart > lengthCount:
        print(
            f'Index out of range error, rowStart is = {rowStart}, and lengthCount is = {lengthCount}')
        # return(None)
    else:
        print("rowStart indexing value is equal to the length; no new values have been added to the sheet.")
        # return(None)


stepThroughSheet(ws, rawRowCount, strList, 1)
print(strList)


def listSort(strList):
    i = 0
    for submissions in strList:
        tempVal = strList[i]
        print(f' the current indexed item is = {tempVal}')
        if 'youtube' or 'youtu.be' in tempVal:
            # ! all values being appended to this list for some reason
            ytList.append(tempVal)
        elif 'spotify' in tempVal:
            spotList.append(tempVal)  # ? not appending values at all?
        else:
            appList.append(tempVal)
        i += 1


listSort(strList)
print(f'youtube list = {ytList}')
print(f'spotify list = {spotList}')
