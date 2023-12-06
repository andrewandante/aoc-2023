import re

def findLowest(time, distance):
    for i in range(time):
        if i * (time - i) > distance:
            return i

def findHighest(time, distance):
    for i in range(time):
        j = time - i
        if j * (time - j) > distance:
            return j

handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

for line in data:
    if line.find('Time:') != -1:
        times = re.findall(r'\d+', line)
        kernTime = ''.join(times)
    if line.find('Distance:') != -1:
        distances = re.findall(r'\d+', line)
        kernDistance = ''.join(distances)

records = dict(zip(times, distances))

valid = 1
for time, distance in records.items():
    lowest = findLowest(int(time), int(distance))
    highest = findHighest(int(time), int(distance))
    valid = valid * (highest - lowest + 1)

print('Part one:')
print(valid)

lowKern = findLowest(int(kernTime), int(kernDistance))
highKern = findHighest(int(kernTime), int(kernDistance))
validKern = highKern - lowKern + 1

print('Part two:')
print(validKern)