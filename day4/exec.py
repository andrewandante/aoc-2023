totalScore = 0
totalCards = 0
cardMap = {}

def calculateScore(game):
    winners = game.split(':')[1].split('|')[0].split(' ')
    candidates = game.split('|')[1].split(' ')
    matchCount = 0
    for candidate in candidates:
        if candidate.isnumeric() == False:
            continue
        if candidate in winners:
            matchCount = matchCount + 1
    if matchCount == 0:
        return 0
    return 2 ** (matchCount - 1)

def matchesCount(game):
    winners = game.split(':')[1].split('|')[0].split(' ')
    candidates = game.split('|')[1].split(' ')
    matchCount = 0
    for candidate in candidates:
        if candidate.isnumeric() == False:
            continue
        if candidate in winners:
            matchCount = matchCount + 1
    return matchCount

def incrementCardMap(gameID):
    if gameID in cardMap:
        cardMap[gameID] = cardMap[gameID] + 1
    else:
        cardMap[gameID] = 1

def processLine(game):
    gameID = int(game.split('Card ')[1].split(':')[0])
    incrementCardMap(gameID)
    score = matchesCount(game)
    for i in range(cardMap[gameID]):
        for j in range(score):
            incrementCardMap(gameID + j + 1)

handle = open("input.txt", "r")
data = handle.read().splitlines()
for game in data:
    totalScore += calculateScore(game)
    processLine(game)
print('Part one:') 
print(totalScore) 

for val in cardMap.values():
    totalCards += val
print('Part two:')
print(totalCards)

handle.close()