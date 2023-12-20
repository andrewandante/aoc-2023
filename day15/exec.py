import re

handle = open("input.txt", "r")
data = handle.read().split(',')
handle.close()

boxes = {}
for i in range(256):
    boxes.update({ i: {}})

def hash_string(thing):
    current = 0
    for char in thing:
        current = current + ord(char)
        current = current * 17
        current = current % 256
    return current

def hashmap_string(spring):
    parts = re.split('[=-]', spring)
    label = parts[0]
    focal = parts[1]

    box = hash_string(label)
    if not focal:
        if label in boxes[box]:
            del(boxes[box][label])
    else:
        boxes[box].update({label: focal})

output = 0
focus_power = 0
for line in data:
    output = output + hash_string(line)
    hashmap_string(line)

for box_id, filled_box in boxes.items():
    base = box_id + 1
    index = 1
    for lens in filled_box.values():
        focus_power = focus_power + (index * int(lens) * base)
        index = index + 1

print('Part one:')
print(output)

print('Part two:')
print(focus_power)