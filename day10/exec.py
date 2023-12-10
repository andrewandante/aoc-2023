pipe_map = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    '7': ['W', 'S'],
    'J': ['N', 'W'],
    'L': ['N', 'E'],
    'F': ['E', 'S'],
    '.': [],
    'S': ['W', 'S'],
    # 'S': ['E', 'S'], USE IF USING EXAMPLE.TXT
}

rowmap = {}
path_corners = []
handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

row = 0
column = 0
start_row = 0
start_col = 0
row_index = 0
current_row = -1
current_col = -1

for row in data:
    valmap = {}
    valIndex = 0
    for char in row:
        valmap[valIndex] = char
        if char == 'S':
            start_row = row_index
            start_col = valIndex
        valIndex = valIndex + 1
    rowmap[row_index] = valmap
    row_index = row_index + 1

steps = 0
entrance = 'S'
while current_row != start_row or current_col != start_col:
    if current_col == -1:
        current_col = start_col
    if current_row == -1:
        current_row = start_row
    
    steps = steps + 1
    pipe = rowmap[current_row][current_col]
    if pipe in ['7', 'L', 'J', 'F', 'S']:
        path_corners.append((current_row, current_col))
    entrances = pipe_map[pipe]
    exit_direction = list(filter(lambda direction: direction != entrance, entrances))[0]
    if exit_direction == 'W':
        current_col = current_col - 1
        entrance = 'E'
    if exit_direction == 'E':
        current_col = current_col + 1
        entrance = 'W'
    if exit_direction == 'S':
        current_row = current_row + 1
        entrance = 'N'
    if exit_direction == 'N':
        current_row = current_row - 1
        entrance = 'S'


print('Part one:')
furthest = steps / 2
print(furthest)

# https://www.geodose.com/2021/09/how-calculate-polygon-area-unordered-coordinates-points-python.html
def explode_xy(xy):
    xl=[]
    yl=[]
    for i in range(len(xy)):
        xl.append(xy[i][0])
        yl.append(xy[i][1])
    return xl,yl

def shoelace_area(x_list,y_list):
    a1,a2=0,0
    x_list.append(x_list[0])
    y_list.append(y_list[0])
    for j in range(len(x_list)-1):
        a1 += x_list[j]*y_list[j+1]
        a2 += y_list[j]*x_list[j+1]
    l=abs(a1-a2)/2
    return l

print('Part two:')
xy_e=explode_xy(path_corners)
A=shoelace_area(xy_e[0],xy_e[1])
print(A - furthest + 1)