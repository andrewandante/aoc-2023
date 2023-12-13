import copy

handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

def get_arrangement(status_line, target):
    in_damaged = False
    damaged_count = 0
    arrangement = []
    for character in status_line:
        if character == '#':
            if in_damaged == False:
                in_damaged = True
            damaged_count = damaged_count + 1
        else:
            if damaged_count > 0:
                arrangement.append(damaged_count)
                if arrangement != target[0:len(arrangement)]:
                    return False
            in_damaged = False
            damaged_count = 0
    if in_damaged == True:
        arrangement.append(damaged_count)
    return arrangement == target

def derive_arrangements(statuses, target):
    print(statuses)
    print(target)
    valid_arrangements = 0
    unknown_count = statuses.count('?')
    for i in range(2**unknown_count):
        _statuses = copy.deepcopy(statuses)
        binary_rep = f'{i:0{unknown_count}b}'
        for j in range(unknown_count):
            _statuses = _statuses.replace('?', '.' if str(binary_rep[j]) == '0' else '#', 1)
        if get_arrangement(_statuses, target) == True:
            valid_arrangements = valid_arrangements + 1
    return valid_arrangements


arrangements = 0
unfolded_arrangements = 0
for line in data:
    [row, contig] = line.split(' ')
    contig_as_array = list(map(int, contig.split(',')))
    combinations = derive_arrangements(row, contig_as_array)
    arrangements = arrangements + combinations
    
    unfolded_row = '?'.join([row, row, row, row, row])
    unfolded_contig = contig_as_array + contig_as_array + contig_as_array + contig_as_array + contig_as_array
    unfolded_combinations = derive_arrangements(unfolded_row, unfolded_contig)
    unfolded_arrangements = unfolded_arrangements + unfolded_combinations

print('Part one:')
print(arrangements)

print('Part two:')
print(unfolded_arrangements)

