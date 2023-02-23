from collections import deque


def read_input():
    f = open("day18_input.txt", "r")
    res = []

    min_x = min_y = min_z = None
    max_x = max_y = max_z = None

    for line in f:
        line = line.strip().split(",")
        x = int(line[0])
        y = int(line[1])
        z = int(line[2])
        min_x = set_min(min_x, x)
        min_y = set_min(min_y, y)
        min_z = set_min(min_z, z)
        max_x = set_max(max_x, x)
        max_y = set_max(max_y, y)
        max_z = set_max(max_z, z)

        res.append((x, y, z))
    f.close()

    return res, (min_x-1, min_y-1, min_z-1), (max_x+1, max_y+1, max_z+1)


def count_sides(cubes_list):
    count = 0

    for i in cubes_list:
        occurence = 6
        x = i[0]
        y = i[1]
        z = i[2]

        if cubes_list.count((x-1, y, z)) > 0:
            occurence -= 1
        if cubes_list.count((x+1, y, z)) > 0:
            occurence -= 1
        if cubes_list.count((x, y-1, z)) > 0:
            occurence -= 1
        if cubes_list.count((x, y+1, z)) > 0:
            occurence -= 1
        if cubes_list.count((x, y, z-1)) > 0:
            occurence -= 1
        if cubes_list.count((x, y, z+1)) > 0:
            occurence -= 1

        count += occurence

    return count


def set_min(current_min, future_min):
    if current_min is None:
        return future_min
    return min(current_min, future_min)


def set_max(current_max, future_max):
    if current_max is None:
        return future_max
    return max(current_max, future_max)


def count_empty(start_cube, end_cube, cubes_list):
    cnt_empty = []
    for x in range(start_cube[0], end_cube[0] + 1):
        for y in range(start_cube[1], end_cube[1] + 1):
            for z in range(start_cube[2], end_cube[2] + 1):
                neigbours = 0
                if cubes_list.count((x+1, y, z)) > 0:
                    neigbours += 1
                if cubes_list.count((x-1, y, z)) > 0:
                    neigbours += 1
                if cubes_list.count((x, y-1, z)) > 0:
                    neigbours += 1
                if cubes_list.count((x, y+1, z)) > 0:
                    neigbours += 1
                if cubes_list.count((x, y, z-1)) > 0:
                    neigbours += 1
                if cubes_list.count((x, y, z+1)) > 0:
                    neigbours += 1

                if neigbours == 6 and cubes_list.count((x, y, z)) == 0:
                    print(f"found: ({x}, {y}, {z})")
                    cnt_empty.append((x, y, z))

    return cnt_empty


def explore_empty(cubes_list, cubes_to_check):
    result = list(cubes_to_check)

    while cubes_to_check:
        c = cubes_to_check.pop()
        x = c[0]
        y = c[1]
        z = c[2]

        if cubes_list.count((x+1, y, z)) == 0:
            cubes_to_check.append((x+1, y, z))
            result.append((x+1, y, z))
        if cubes_list.count((x-1, y, z)) == 0:
            cubes_to_check.append((x-1, y, z))
            result.append((x-1, y, z))
        if cubes_list.count((x, y-1, z)) == 0:
            cubes_to_check.append((x, y+1, z))
            result.append((x, y+1, z))
        if cubes_list.count((x, y+1, z)) == 0:
            cubes_to_check.append((x, y-1, z))
            result.append((x, y-1, z))
        if cubes_list.count((x, y, z-1)) == 0:
            cubes_to_check.append((x, y, z-1))
            result.append((x, y, z-1))
        if cubes_list.count((x, y, z+1)) == 0:
            cubes_to_check.append((x, y, z+1))
            result.append((x, y, z+1))

    return result


def count_inner_cubes(cubes_set):
    cubes_list = list(cubes_set)
    cl_x = sorted(cubes_list, key=lambda x: x[0])
    cl_y = sorted(cubes_list, key=lambda x: x[1])
    cl_z = sorted(cubes_list, key=lambda x: x[2])

    print(cl_x)
    print(cl_y)
    print(cl_z)

    set_inner = set()
    last_elem = len(cubes_list) - 1

    for i in cubes_list:
        index_x = cl_x.index(i)
        index_y = cl_y.index(i)
        index_z = cl_z.index(i)
        #print(f"{index_x} - {index_y} - {index_z}")
        #print(f"{index_x!=0} - {index_y!=0} - {index_z!=0}")

        if index_x > 0 and index_x < last_elem and index_y > 0 and index_y < last_elem and index_z > 0 and index_z < last_elem:
            set_inner.add(i)
            print(f"elem: {i} at {index_x} - {index_y} - {index_z}")

    return set_inner


def get_neighbours(cube, min_cube, max_cube):
    x = cube[0]
    y = cube[1]
    z = cube[2]

    ret = set()
    if (x > min_cube[0]):
        ret.add((x-1, y, z))
    if (x < max_cube[0]):
        ret.add((x+1, y, z))
    if (y > min_cube[1]):
        ret.add((x, y-1, z))
    if (y < max_cube[1]):
        ret.add((x, y+1, z))
    if (z > min_cube[2]):
        ret.add((x, y, z-1))
    if (z < max_cube[2]):
        ret.add((x, y, z+1))

    return ret


def flood_fill(min_cube, max_cube, figure_cubes):
    steam = (min_cube[0], min_cube[1], min_cube[2])
    steamed_cubes = set()
    queue = deque()
    queue.append(min_cube)

    while queue:
        curr_item = queue.pop()
        if curr_item not in figure_cubes and curr_item not in steamed_cubes:
            steamed_cubes.add(curr_item)
            neigh_list = get_neighbours(curr_item, min_cube, max_cube)
            for i in neigh_list:
                if i not in figure_cubes:
                    queue.append(i)

    return steamed_cubes


min_cube = (-1, -1, -1)
max_cube = (-1, -1, -1)
cubes, min_cube, max_cube = read_input()

all_cubes = set()
for i in range(min_cube[0], max_cube[0] + 1):
    for j in range(min_cube[1], max_cube[1] + 1):
        for k in range(min_cube[2], max_cube[2] + 1):
            all_cubes.add((i, j, k))

all_cubes_cnt = (max_cube[0] - min_cube[0] + 1) * (max_cube[1] -
                                                   min_cube[1] + 1) * (max_cube[2] - min_cube[2] + 1)

# print(cubes)
print(f"min: {min_cube}, max: {max_cube}")

cnt = count_sides(cubes_list=cubes)

steamed = flood_fill(min_cube, max_cube, cubes)
# print(steamed)

steamed_cubes_cnt = len(steamed)
droplet_cnt = len(cubes)

print(
    f"Total: {all_cubes_cnt}, steamed: {steamed_cubes_cnt} droplet:  {droplet_cnt} diff: {all_cubes_cnt - steamed_cubes_cnt - droplet_cnt}")

droplet = all_cubes - steamed
cnt_drop = count_sides(list(droplet))
print(cnt_drop)
