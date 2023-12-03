gearMap = {}
productTotal = 0

def checkForSymbol(rowmap, row, start, end, number):
    for looprowindex, looprow in rowmap.items():
        if looprowindex < row - 1 or looprowindex > row + 1:
            continue
        for valIndex, val in looprow.items():
            if valIndex < start - 1 or valIndex > end + 1:
                continue
            if val == '*':
                mapkey = str(looprowindex) + "_" + str(valIndex)
                if mapkey in gearMap:
                    gearMap[mapkey].append(number)
                else:
                    gearMap[mapkey] = [number]
                return True
            if val != '.' and val.isnumeric() == False:
                return True
    return False


handle = open("input.txt", "r")
data = handle.read().splitlines()

returnTotal = 0
rowMap = {}
rowIndex = 0

for row in data:
    valmap = {}
    valIndex = 0
    for char in row:
        valmap[valIndex] = char
        valIndex = valIndex + 1
    rowMap[rowIndex] = valmap
    rowIndex = rowIndex + 1

numberStartIndex = -1
numberEndIndex = -1
numberString = ''
for loopRowIndex, loopRow in rowMap.items():
    for valIndex, val in loopRow.items():
        if val.isnumeric():
            if numberStartIndex == -1:
                numberStartIndex = valIndex
            numberEndIndex = valIndex
            numberString += val
        else:
            if numberEndIndex > -1:
                if checkForSymbol(rowMap, loopRowIndex, numberStartIndex, numberEndIndex, numberString) == True:
                    returnTotal += int(numberString)
            numberStartIndex = -1
            numberEndIndex = -1
            numberString = ''

print("Part one:")
print(returnTotal)

for gear in gearMap.values():
    if len(gear) == 2:
        productTotal += int(gear[0]) * int(gear[1])

print("Part two:")
print(productTotal)
handle.close()