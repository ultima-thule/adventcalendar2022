
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


points, mapa, min_point, max_point = read_input()
# print(points)
print(mapa)
print(
    f"MIN {min_point} MAX{max_point}")


cnt = 0
y_dest = 2000000
#y_dest = 20
items = set()
points_items = set()

for p in mapa.items():
    difference = abs(p[0][1] - y_dest)
    width = p[1] - difference
    add_items = 2*p[1] + 1 - 2*difference

    if width > 0:
        min_range = min(p[0][0]-width, p[0][0]+width)
        max_range = max(p[0][0]-width, p[0][0]+width)

        #print(f"point: {p[0]} odl od B: {p[1]} odl w pionie: {difference} width: {width}")
        #print(f"from {min_range} to {max_range}")

        items.add(range(min_range, max_range))

        for i in range(min_range, max_range + 1):
            points_items.add(i)

print(items)
print(points_items)
print(len(points_items)-1)
