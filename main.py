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
    for links in tempList[i]:
        if spotString in tempList[i][n]:
            spotCount + 1
            n += 1
        elif ytString in tempList[i][n]:
            ytCount + 1
            n += 1
        else:
            n += 1
    i += 1

print(f'Spotify: {spotCount}')
print(f'YT: {ytCount}')
