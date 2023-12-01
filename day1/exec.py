import re

handle = open("input.txt", "r")
data = handle.read().splitlines()

total = 0
for value in data:
    first = re.search(r'\d', value)
    last = re.search(r'\d', value [::-1])
    total += (10*int(first.group()))
    total += int(last.group())

print('part one:')
print(total)

newtotal = 0
numwords = {
    '1': 'one',
    '2': 'two',
    '3': 'three', 
    '4': 'four',
    '5': 'five', 
    '6': 'six',
    '7': 'seven', 
    '8': 'eight',
    '9': 'nine'
}

strpos = {}
for value in data:
    strpos.clear()
    for num, word in numwords.items():
        numpos = value.find(num)
        if numpos != -1:
            strpos[numpos] = int(num)
            strpos[value.rfind(num)] = int(num)
        wordpos = value.find(word)
        if wordpos != -1:
            strpos[wordpos] = int(num)
            strpos[value.rfind(word)] = int(num)

    sortedlist = sorted(strpos.items())
    first = 0
    last = 0
    for key,val in sortedlist:
        if first == 0:
            first = 10 * val
        last = val
    newtotal += first
    newtotal += last
print('part two:')
print(newtotal)
handle.close()