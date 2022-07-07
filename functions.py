# define a function to step through the rows in the sheet based off of the acquired start value from the save file
def stepThroughSheet(worksheet, lengthCount, aList, startNum):
    rowStart = int(startNum)
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


# define a function for sorting based off platform submission
def listSort(strList, ytList, spotList, appList):
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


def writeFile(filename, aList):
    with open(filename, 'a') as openFile:
        i = 0
        for item in aList:
            strVal = aList[i]
            openFile.write(strVal)
            openFile.write(', unchecked')
            openFile.write('\n')
            i += 1
    print(f'Contents written to {filename}')


def getStart(filename):
    with open(filename, 'r') as saveFile:
        savedValue = saveFile.readline()
        print(f'{savedValue} is the last saved length of the submissions form.')
        return savedValue


def compareLength(oldNum, currentLength, filename):
    oldLength = int(oldNum)
    if oldLength > currentLength:
        print(f'Old length exceeds current... was a previous submission removed?')
    elif currentLength > oldLength:
        print(
            f'Current form list exceeds length of recorded... New submissions are present.')
        with open(filename, 'w') as newRecord:
            newRecord.write(str(currentLength))
    else:
        print(f'Current and Recorded length are equal... No new submissions.')


def checkIn(filename, aList):
    with open(filename, 'r') as listFile:
        pass
