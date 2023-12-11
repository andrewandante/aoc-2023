row_map = {}
galaxies = {}
galaxy_pairs = []
rows_with_galaxies = []
cols_with_galaxies = []
handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

row = 0
column = 0
row_index = 0
galaxy_count = 0

for row in data:
    valmap = {}
    val_index = 0
    for char in row:
        valmap[val_index] = char
        if char == '#':
            galaxy_count = galaxy_count + 1
            galaxies.update({ galaxy_count: [row_index, val_index]})
            rows_with_galaxies.append(row_index)
            cols_with_galaxies.append(val_index)
        val_index = val_index + 1
    row_map[row_index] = valmap
    row_index = row_index + 1

def calculate_distance(beginning, end, expansion):
    beg_row = beginning[0]
    beg_col = beginning[1]
    end_row = end[0]
    end_col = end[1]

    distance = 0
    if beg_row < end_row:
        for i in range(end_row - beg_row):
            if (beg_row + i) not in rows_with_galaxies:
                distance = distance + expansion
            else:
                distance = distance + 1
    if beg_row > end_row:
        for j in range(beg_row - end_row):
            if (end_row + j) not in rows_with_galaxies:
                distance = distance + expansion
            else:
                distance = distance + 1
    if beg_col < end_col:
        for i in range(end_col - beg_col):
            if (beg_col + i) not in cols_with_galaxies:
                distance = distance + expansion
            else:
                distance = distance + 1
    if beg_col > end_col:
        for j in range(beg_col - end_col):
            if (end_col + j) not in cols_with_galaxies:
                distance = distance + expansion
            else:
                distance = distance + 1

    return distance
path_total = 0
old_path_total = 0
for sgi, start_galaxy in galaxies.items():
    for egi, end_galaxy in galaxies.items():
        if (sgi, egi) not in galaxy_pairs and (egi, sgi) not in galaxy_pairs:
            path_total = path_total + calculate_distance(start_galaxy, end_galaxy, 2)
            old_path_total = old_path_total + calculate_distance(start_galaxy, end_galaxy, 1000000)
            galaxy_pairs.append((sgi, egi))

print('Part one:')
print(path_total)

print('Part two:')
print(old_path_total)