def read_input():
    f = open("day17b_input.txt", "r")
    res = ""
    for line in f:
        line = line.strip()
        res = res.join(line)
    f.close()

    return res


def calc_shape_startpos(template, max_height):
    ret = []
    for t in template:
        ret.append((t[0] + 2, t[1] + max_height + 1 + 3))
    return ret


def move_right(shape, used_points):
    max_right = max(p[0] for p in shape)

    ret = []
    for t in shape:
        ret.append((t[0]+1, t[1]))

    new_shape = set(ret)
    # print(new_shape)
    diff_set = new_shape - used_points
    # print(diff_set)

    # print(max_right)
    if max_right < 6 and len(diff_set) == len(shape):
        return ret, False
    else:
        return shape, True


def move_left(shape, used_points):
    min_left = min(p[0] for p in shape)

    ret = []
    for t in shape:
        ret.append((t[0]-1, t[1]))

    new_shape = set(ret)
    # print(new_shape)
    diff_set = new_shape - used_points
    # print(diff_set)

    if min_left > 0 and len(diff_set) == len(shape):
        return ret, False
    else:
        return shape, True


def move_down(shape, used_points):
    min_bottom = min(p[1] for p in shape)
    # print(min_bottom)

    ret = []
    for t in shape:
        ret.append((t[0], t[1]-1))

    new_shape = set(ret)
    # print(new_shape)
    diff_set = new_shape - used_points
    # print(diff_set)

    if len(diff_set) == len(shape):
        return ret, False
    else:
        return shape, True


def max_used_y(used_points, x):
    max_y = -1
    if used_points:
        max_y = max(i[1] for i in used_points if i[0] == x)
    return max_y


def print_board(points):
    str_res = ""
    str_temp = ""
    for i in range(0, 15):
        str_temp = ""
        for j in range(0, 7):
            if points.count((j, i)) > 0:
                str_temp += "#"
            else:
                str_temp += "."
        str_res = str_temp + "\n" + str_res
    return str_res


shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]]


floor = 0

res = read_input()

iter_cnt = 0
shape_cnt = 0

used_points = set([(0, -1), (1, -1), (2, -1),
                  (3, -1), (4, -1), (5, -1), (6, -1)])

while iter_cnt < len(res):
    shape_template = shapes[shape_cnt % 5]
    blocked_move = False
    blocked = False
    shape = calc_shape_startpos(
        shape_template, floor)
    print(print_board(list(shape)))

    print(f"start shape: {shape}")
    # print(shape)

    while not blocked and iter_cnt < len(res):
        move = res[iter_cnt]
        if move == ">":
            shape, blocked_move = move_right(shape, used_points)
            print(print_board(list(shape)))
        elif move == "<":
            shape, blocked_move = move_left(shape, used_points)
            print(print_board(list(shape)))

        print(f"move {move} shape: {shape} blocked: {blocked_move}")

        iter_cnt += 1

        shape, blocked = move_down(shape, used_points)
        print(print_board(list(shape)))
        print(f"move down shape: {shape} blocked: {blocked}")
        if blocked:
            for i in shape:
                used_points.add(i)
            floor = max([x[1] for x in used_points])
            print(used_points)
            print(f"floor: {floor}")
            print("--------------------------------------")
            print(print_board(list(used_points)))

    shape_cnt += 1

print(sorted(used_points))
