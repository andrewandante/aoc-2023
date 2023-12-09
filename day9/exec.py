import re
    
def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

def next_in_seq(sequence, reverse=False):
    chain = {
        0: sequence
    }
    breakout = False
    index = 0
    while breakout == False:
        new_seq = []
        for i in range(len(chain[index]) - 1):
            new_seq.append(int(sequence[i + 1]) - int(sequence[i]))
        chain.update({index + 1: new_seq})
        index = index + 1
        sequence = new_seq
        if all_equal(chain[index]):
            breakout = True
    
    if reverse == False:
        chain[index].append(int(chain[index][-1]))
        for j in range(len(chain)):
            if j == 0:
                continue
            chain[index-j].append(int(chain[index-j][-1]) + int(chain[index-j+1][-1]))

        return chain[0][-1]
    else:
        chain[index].reverse()
        chain[index].append(int(chain[index][-1]))
        for j in range(len(chain)):
            if j == 0:
                continue
            chain[index-j].reverse()
            chain[index-j].append(int(chain[index-j][-1]) - int(chain[index-j+1][-1]))

        return chain[0][-1]

handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

total = 0
for line in data:
    base_sequence = list(map(int, re.findall(r'-?\d+', line)))
    next_val = next_in_seq(base_sequence)
    total = total + next_val

print('Part one:')
print(total)

total = 0
for line in data:
    base_sequence = list(map(int, re.findall(r'-?\d+', line)))
    next_val = next_in_seq(base_sequence, True)
    total = total + next_val


print('Part two:')
print(total)