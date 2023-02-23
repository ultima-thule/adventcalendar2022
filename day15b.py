
def read_input():
    min_point = (0, 0)
    max_point = (0, 0)

    f = open("day15_input.txt", "r")
    res = set()
    dist = {}
    for line in f:
        line = line.strip().replace("Sensor at ", "").replace(" closest beacon is at ", "")
        results = line.split(":")
        sensor = tuple(eval(results[0].replace("x=", "").replace("y=", "")))
        beacon = tuple(eval(results[1].replace("x=", "").replace("y=", "")))
        max_distance = calc_distance(sensor, beacon)
        min_point, max_point = check_boudaries(
            sensor, beacon, min_point, max_point)
        res.add((sensor))
        res.add((beacon))
        dist[sensor] = max_distance
        # print(f"sensor: {sensor} beacon: {beacon} distance: {max_distance}")
    f.close()
    return res, dist, min_point, max_point


def calc_distance(point_x, point_y):
    return abs(point_x[0] - point_y[0]) + abs(point_x[1] - point_y[1])


def check_boudaries(point_x, point_y, min_point, max_point):
    if min(point_x[0], point_y[0]) < min_point[0]:
        min_point = (min(point_x[0], point_y[0]),  min_point[1])
    if min(point_x[1], point_y[1]) < min_point[1]:
        min_point = (min_point[0], min(point_x[1], point_y[1]))

    if max(point_x[0], point_y[0]) > max_point[0]:
        max_point = (max(point_x[0], point_y[0]),  max_point[1])
    if max(point_x[1], point_y[1]) > max_point[1]:
        max_point = (max_point[0], max(point_x[1], point_y[1]))

    return min_point, max_point


def exclude(point):
    # print(point)
    to_exclude = set()
    dist = point[1]
    a_start = point[0][0] - dist
    a_end = point[0][0] + dist
    b_start = point[0][1] - dist
    b_end = point[0][1] + dist

    print(
        f"point:{point} distance: {dist} from {(a_start, a_end)} to {(b_start, b_end)}")

    for i in range(a_start, a_end):
        for j in range(b_start, b_end):
            dist = calc_distance(point[0], (i, j))
            if dist <= point[1]:
                print(f"from {point[0]} to {(i, j)} distance: {dist}")
                to_exclude.add((i, j))
    # print(to_exclude)
    # print("-----------------")
    return to_exclude


def exclude_points(points, mapa):
    for m in mapa.items():
        points = points.union(exclude(m))
    return points


def overlap_range(input):
    # print(input)
    res = []
    for begin, end in sorted(input):
        if res and res[-1][1] >= begin - 1:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([begin, end])

    return res


points, mapa, min_point, max_point = read_input()
# print(points)
# print(mapa)
# print(f"MIN {min_point} MAX{max_point}")


cnt = 0
y_dest = 4000000
#y_dest = 20
items = []
points_items = set()

y_coord = -1
x_coord = -1

total = int((1 + y_dest) / 2 * y_dest)
# print(total)

print(3405562 * 4000000 + 3246513)

for y in range(0, y_dest+1):
    break
    print(f"linia {y}")
    points_items = set()
    items = []

    for p in mapa.items():
        difference = abs(p[0][1] - y)
        width = p[1] - difference
        add_items = 2*p[1] + 1 - 2*difference

        if width > 0:
            min_range = max(min(p[0][0]-width, p[0][0]+width), 0)
            max_range = min(max(p[0][0]-width, p[0][0]+width), y_dest)

            # print(f"point: {p[0]} odl od B: {p[1]} odl w pionie: {difference} width: {width}")
            #print(f"from {min_range} to {max_range}")

            items.append((min_range, max_range))
            #items.add(range(min_range, max_range))

            # for i in range(min_range, max_range + 1):
            #     points_items.add(i)
    # print(items)
    res = overlap_range(items)
    if len(res) != 1:
        print(f"y: {y} ilosc pusta: {res}")
        break
        # x_coord = total - sum(points_items)
        # print(f"{x_coord}")

        # print(points_items)

        # ilosc = len(points_items) - 1
        # if ilosc == y_dest:
        #     pass
        #     print(f"y: {y} ilosc dokładna: {ilosc}")
        # else:
        #     print(f"y: {y} ilosc pusta: {ilosc}")
        #     x_coord = total - sum(points_items)
        #     y_coord = y
        #     break

        # print(items)
        # print(points_items)
        # print(len(points_items)-1)

# print(x_coord)
# print(y_coord)
