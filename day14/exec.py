handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

col_vals = []
col_max = {}

row_index = 0
for line in data:
    col_index = 0
    for char in line:
        if col_index not in col_max:
            col_max.update({col_index: 0})
        if char == '#':
            col_max.update({col_index: row_index + 1})
        if char == 'O':
            col_vals.append(col_max[col_index])
            col_max.update({col_index: col_max[col_index] + 1})
        col_index = col_index + 1
    row_index = row_index + 1

result = 0
for val in col_vals:
    load = row_index - val
    result = result + load

print('Part one:')
print(result)




