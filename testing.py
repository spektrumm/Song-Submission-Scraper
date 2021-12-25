sheetString = 'https://open.spotify.com/track/5B9t3xqRqNzyb7MDNXOReG?si=91cd282737d8494c, https://www.youtube.com/watch?v=D1NdGBldg3w, https://open.spotify.com/track/2fhAEQ0rBKl8bY8PoEmZYZ?si=0b7495e7f25a42e2'
ytString = 'youtube'
spotString = 'spotify'
spotCount = 0
ytCount = 0
tempList = []

noSpace = sheetString.replace(' ', '')
splitLinks = noSpace.split(',')

tempList.append(splitLinks)

print(tempList)
i = 0
n = 0
for submissions in tempList:
    for links in splitLinks:
        if spotString in splitLinks[n]:
            print(splitLinks[n])
            spotCount += 1
            n += 1
        elif ytString in splitLinks[n]:
            ytCount += 1
            n += 1
        else:
            n += 1

print(f'Spotify: {spotCount}')
print(f'YT: {ytCount}')

print(splitLinks)
numTest = spotCount + 1
print(numTest)


async def check(ctx):

    updatedRowCount = len(sheet_instance.get_all_values())

    timestampChk = sheet_instance.cell(col=1, row=updatedRowCount)
    categoryChk = sheet_instance.cell(col=2, row=updatedRowCount)
    usernameChk = sheet_instance.cell(col=3, row=updatedRowCount)

    convertTime = str(timestampChk)
    convertCat = str(categoryChk)
    convertUser = str(usernameChk)

    if updatedRowCount > rawRowCount:
        await ctx.send(f'New bug report! **Timestamp:** {convertTime[13:-2]}, **Category:** {convertCat[12:-2]}, **Submitted by:** {convertUser[12:-2]} **Link:** https://docs.google.com/forms/d/1tU7OR2U0LOkB6cuC-JppTNyxjcLBsewWpBp2Meg8LwE/edit#responses')
        print('New bug report!')
    else:
        await ctx.send('No new bug reports.')
        print('No new bug reports.')
