import re

grossMap = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': [],
}

def convert(mapper, val, reverse=False):
    val = int(val)

    for candidate in grossMap[mapper]:
        if reverse == False:
            if val >= int(candidate['srcRangeStart']) and val <= int(candidate['srcRangeStart']) + int(candidate['rangeLength']):
                distance = val - int(candidate['srcRangeStart'])
                return str(int(candidate['destRangeStart']) + distance)
        else:
            if val >= int(candidate['destRangeStart']) and val <= int(candidate['destRangeStart']) + int(candidate['rangeLength']):
                distance = val - int(candidate['destRangeStart'])
                return str(int(candidate['srcRangeStart']) + distance)
    return str(val)

handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

maptype = ''
allLocations = []
seedRanges = []
for line in data:
    if line == '':
        maptype = ''
        converters = []
        continue
    if line.find('seeds:') != -1:
        seeds = re.findall(r'\d+', line)
        seedStart = -1
        for seed in seeds:
            if seedStart == -1:
                seedStart = int(seed)
                continue
            seedRanges.append({
                'start': seedStart,
                'end': seedStart + int(seed) - 1
            })
            seedStart = -1
                
        continue
    if line.find('map:') != -1:
        maptype = line.split(' map:')[0]
        continue
    if maptype != '':
        converters = re.findall(r'\d+', line)
        destRangeStart = int(converters[0])
        srcRangeStart = int(converters[1])
        rangeLength = int(converters[2])
        grossMap[maptype].append({
            'destRangeStart': destRangeStart,
            'srcRangeStart': srcRangeStart,
            'rangeLength': rangeLength
        })

for seed in seeds:
    soil = convert('seed-to-soil', seed)
    fertilizer = convert('soil-to-fertilizer', soil)
    water = convert('fertilizer-to-water', fertilizer)
    light = convert('water-to-light', water)
    temp = convert('light-to-temperature', light)
    humidity = convert('temperature-to-humidity', temp)
    location = convert('humidity-to-location', humidity)
    allLocations.append(int(location))

allLocations.sort()
print('Part one:')
print(allLocations[0])

location = 0
breakOut = False
while breakOut == False:
    humidity = convert('humidity-to-location', location, True)
    temp = convert('temperature-to-humidity', humidity, True)
    light = convert('light-to-temperature', temp, True)
    water = convert('water-to-light', light, True)
    fertilizer = convert('fertilizer-to-water', water, True)
    soil = convert('soil-to-fertilizer', fertilizer, True)
    seed = int(convert('seed-to-soil', soil, True))
    for ranges in seedRanges:
        if seed >= int(ranges['start']) and seed <= int(ranges['end']):
            print('Part two:')
            print(location)
            breakOut = True
            break
    location = location + 1
