f = open("day8_input.txt", "r")

grid = []
results = []

row_no = 0
col_no = 0

for line in f:
    grid.append([])
    results.append([])

    line = line.strip()
    col_no = len(line)

    col = 0
    for height in line:
        grid[row_no].append(int(height))
        results[row_no].append([])
        results[row_no][col].append(int(height))
        col += 1
    row_no += 1

f.close()


for i in range(row_no):
    left = 0

    for j in range(col_no):

        #print(f"LEFT Row: {i} Col: {j} Value: {grid[i][j]} Max: {left}")
        results[i][j].append(left)

        left = max(left, grid[i][j])

for i in range(row_no):
    right = 0

    for j in range(col_no):

        #print(f"RIGHT Row: {i} Col: {j} Value: {grid[i][-j-1]} Max: {right}")
        results[i][-j-1].append(right)

        right = max(right, grid[i][-j-1])

for i in range(col_no):
    top = 0

    for j in range(row_no):

        #print(f"TOP Row: {j} Col: {i} Value: {grid[j][i]} Max: {top}")
        results[j][i].append(top)

        top = max(top, grid[j][i])

for i in range(col_no):
    bottom = 0

    for j in range(row_no):

        #print(f"BOTTOM Row: {j} Col: {i} Value: {grid[-j-1][i]} Max: {bottom}")
        results[-j-1][i].append(bottom)

        bottom = max(bottom, grid[-j-1][i])

print(results)

visible = 0
for i in range(row_no):
    for j in range(col_no):
        tree_height = results[i][j][0]
        if i == 0 or j == 0 or i == row_no-1 or j == col_no-1:
            visible += 1
            #print(f"Skrajne drzewo {i} {j}")
        elif tree_height > results[i][j][1] or tree_height > results[i][j][2] or tree_height > results[i][j][3] or tree_height > results[i][j][4]:
            visible += 1
            #print(f"Drzewo {i} {j}")


print(visible)
