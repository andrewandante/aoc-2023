from math import lcm

handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

pattern = data.pop(0)
ltrain = {}
rtrain = {}
keychain = []

for line in data:
    if line == '':
        continue
    key = line.split(' = ')[0]
    left = line.split('(')[1].split(',')[0]
    right = line.split(', ')[1].split(')')[0]
    keychain.append(key)
    ltrain[key] = left
    rtrain[key] = right

index = 'AAA'
steps = 0
pattern_index = 0
while index != 'ZZZ':
    train = pattern[pattern_index]
    if train == 'L':
        index = ltrain[index]
    elif train == 'R':
        index = rtrain[index]
    steps = steps + 1
    pattern_index = pattern_index + 1
    if pattern_index >= len(pattern):
        pattern_index = 0

print('Part one:')
print(steps)

def find_next_z(g_key):
    offset = 0
    g_steps = 0
    while g_key[-1] != 'Z':
        g_train = pattern[offset]
        if g_train == 'L':
            g_key = ltrain[g_key]
        elif g_train == 'R':
            g_key = rtrain[g_key]
        offset = offset + 1
        g_steps = g_steps + 1
        if offset >= len(pattern):
            offset = 0
    return g_steps

factors = []
for ghost_key in keychain:
    if ghost_key[-1] != 'A':
        continue
    factors.append(find_next_z(ghost_key))

print('Part 2:')
print(lcm(*factors))