handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

def reflects(patterns, pivot):
    length = len(patterns)
    loops = min(length - pivot, pivot)
    for l in range(1, loops):
        if patterns[pivot - l] != patterns[pivot + 1 + l]:
            return False
    return True

def process(rows, cols):
    for index, row in rows.items():
        if index + 1 in rows and rows[index + 1] == row and reflects(rows, index):
            return index * 100
    for c_index, col in cols.items():
        if c_index + 1 in cols and cols[c_index + 1] == col and reflects(cols, c_index):
            return c_index

pat_rows = {}
pat_cols = {}
row_index = 1
col_index = 1
return_val = 0
for row in data:
    if row == '':
        row_index = 1
        col_index = 1
        return_val = return_val + process(pat_rows, pat_cols)
        pat_rows = {}
        pat_cols = {}
    else:
        pat_rows.update({row_index: row})
        row_index = row_index + 1
        col_index = 1
        for char in row:
            if col_index in pat_cols:
                pat_cols[col_index] = pat_cols[col_index] + char
            else:
                pat_cols.update({col_index: char})
            col_index = col_index + 1


print('Part one:')
print(return_val)