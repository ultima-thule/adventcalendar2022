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
    for j in range(col_no):
        current_element = results[i][j][0]
        #print(f"i: {i} j: {j} current elem: {current_element}")

        distance_left = 0
        for ind_j in range(j, 0, -1):
            left_element = results[i][ind_j-1][0]
            #print(f"Element to left: {left_element}")
            if left_element < current_element:
                distance_left += 1
                #print(f"distance_left: {distance_left}")
            else:
                distance_left += 1
                #print(f"distance_left: {distance_left}")
                break

        results[i][j].append(distance_left)

        distance_right = 0
        for ind_j in range(j + 1, col_no):
            right_element = results[i][ind_j][0]
            #print(f"Element to right: {right_element}")
            if right_element < current_element:
                distance_right += 1
                #print(f"distance_right: {distance_right}")
            else:
                distance_right += 1
                #print(f"distance_right: {distance_right}")
                break

        results[i][j].append(distance_right)

        distance_top = 0
        for ind_i in range(i-1, -1, -1):
            #print(f"ind_i: {ind_i}")
            top_element = results[ind_i][j][0]
            #print(f"Element to top: {top_element}")
            if top_element < current_element:
                distance_top += 1
                #print(f"distance_top 1: {distance_top}")
            else:
                distance_top += 1
                #print(f"distance_top 2: {distance_top}")
                break

        results[i][j].append(distance_top)

        distance_bottom = 0
        for ind_i in range(i + 1, row_no):
            #print(f"ind_i: {ind_i}")
            bottom_element = results[ind_i][j][0]
            #print(f"Element to bottom: {bottom_element}")
            if bottom_element < current_element:
                distance_bottom += 1
                #print(f"distance_bottom 1: {distance_bottom}")
            else:
                distance_bottom += 1
                #print(f"distance_bottom 2: {distance_bottom}")
                break

        results[i][j].append(distance_bottom)


# print(results)

max_score = 0

for i in range(row_no):
    for j in range(col_no):
        scenic_score = results[i][j][1] * results[i][j][2] * \
            results[i][j][3] * results[i][j][4]
        if scenic_score > max_score:
            max_score = scenic_score

print(max_score)
