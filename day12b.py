from collections import deque

start_indexes = {}


def read_input():
    start = ''
    end = ''
    array = []
    f = open("day12_input.txt", "r")
    x_cnt = 0
    y_cnt = 0
    for line in f:
        line = line.strip()
        array.append([])
        for x in line:
            if x == "S":
                start = f"{x_cnt}_{y_cnt}"
                x = 'a'
            elif x == "E":
                end = f"{x_cnt}_{y_cnt}"
                x = 'z'
            array[x_cnt].append(x)
            if x == 'a':
                start_indexes[f"{x_cnt}_{y_cnt}"] = INFINITE_DIST
            y_cnt += 1
        x_cnt += 1
        y_cnt = 0
    f.close()

    return array, start, end


def find_min(que, dist_array):
    minimum = None
    min_index = ""
    for q in que:
        if minimum == None:
            minimum = dist_array[q]
            min_index = q
            continue
        if dist_array[q] < minimum:
            minimum = dist_array[q]
            min_index = q
    return min_index


def calculate_distance(u, v):
    u_indices = u.split("_")
    u_x = int(u_indices[0])
    u_y = int(u_indices[1])

    v_indices = v.split("_")
    v_x = int(v_indices[0])
    v_y = int(v_indices[1])

    if u_x < 0 or u_y < 0 or v_x < 0 or v_y < 0:
        return INFINITE_DIST
    u_terrain = terrain[u_x][u_y]
    v_terrain = terrain[v_x][v_y]

    #distance = abs(ord(u_terrain) - ord(v_terrain))
    distance = ord(v_terrain) - ord(u_terrain)
    #print(f"from {u_terrain} to {v_terrain} distance {distance}")

    if distance <= 1:
        return 1
    else:
        return INFINITE_DIST


terrain = []
INFINITE_DIST = 100000000000000
SKIP_DIST = 200000000000000

start_index = ""
end_index = ""

terrain, start_index, end_index = read_input()
#print(f"start: {start_index} end: {end_index}")

print(start_indexes)

max_x = len(terrain)
max_y = len(terrain[0])
#print(f"max_x: {max_x} max_y: {max_y}")


def Dijkstra(start_from):
    distance = {}
    prev = {}
    skip = {}

    queue = deque()

    for i in range(max_x):
        for j in range(max_y):
            distance[f"{i}_{j}"] = INFINITE_DIST
            prev[f"{i}_{j}"] = None
            queue.append(f"{i}_{j}")
    distance[start_from] = 0

    while queue:
        u = find_min(queue, distance)
        # print(u[0])
        value = queue.remove(u)
        skip[u] = ''
        indices = u.split("_")
        x = int(indices[0])
        y = int(indices[1])
        neighbours = [f"{x}_{y-1}", f"{x}_{y+1}",
                      f"{x-1}_{y}", f"{x+1}_{y}"]

        for v in neighbours:
            if v in queue:
                skip[v] = ''
                alt = distance[u] + calculate_distance(u, v)
                if alt < distance[v]:
                    distance[v] = alt
                    prev[v] = u

    path_queue = deque()

    u = end_index
    if prev[u] != None or prev[u] == start_index:
        try:
            while u:
                path_queue.appendleft(u)
                u = prev[u]
        except:
            pass

    # print(path_queue)
    length = len(path_queue) - 1
    if length <= 0:
        for i in skip.keys():
            if start_indexes.get(i) is not None:
                start_indexes[i] = SKIP_DIST
    return length


for i in start_indexes.keys():
    print(f"==> index: {i} start")
    val = Dijkstra(i)
    if val > 0:
        start_indexes[i] = val
    print(f"index: {i} calculated value: {val}")


print(start_indexes)
mini = min(start_indexes, key=start_indexes.get)
print(start_indexes[mini])
