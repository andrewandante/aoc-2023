import re

def isValidGame(game):
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    for pull in game.split(';'):
        for cubes in pull.split(','):
            if cubes.find('green') != -1 and int(re.search(r'\d+', cubes).group()) > maxGreen:
                return False
            if cubes.find('red') != -1 and int(re.search(r'\d+', cubes).group()) > maxRed:
                return False
            if cubes.find('blue') != -1 and int(re.search(r'\d+', cubes).group()) > maxBlue:
                return False
    return True

def IGotThaPowa(game):
    minRed = 1
    minGreen = 1
    minBlue = 1
    for pull in game.split(';'):
        for cubes in pull.split(','):
            candidate = int(re.search(r'\d+', cubes).group())
            if cubes.find('green') != -1:
                minGreen = max(minGreen, candidate)
            if cubes.find('red') != -1:
                minRed = max(minRed, candidate)
            if cubes.find('blue') != -1:
                minBlue = max(minBlue, candidate)
    return minRed * minGreen * minBlue

handle = open("input.txt", "r")
data = handle.read().splitlines()

idTotal = 0
powerTotal = 0
for game in data:
    gameId = game[5:game.index(":")]
    gameData = game[6+len(gameId):]
    if isValidGame(gameData):
        idTotal += int(gameId)
    powerTotal += IGotThaPowa(gameData)
print('Part One:')
print(idTotal)
print('Part Two:')
print(powerTotal)

handle.close()

