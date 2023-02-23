from collections import deque


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
            y_cnt += 1
        x_cnt += 1
        y_cnt = 0
    f.close()

    return array, start, end


def find_min(que):
    minimum = None
    min_index = ""
    for q in que:
        if minimum == None:
            minimum = distance[q]
            min_index = q
            continue
        if distance[q] < minimum:
            minimum = distance[q]
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

start_index = ""
end_index = ""

terrain, start_index, end_index = read_input()
#print(f"start: {start_index} end: {end_index}")

max_x = len(terrain)
max_y = len(terrain[0])
#print(f"max_x: {max_x} max_y: {max_y}")

distance = {}
prev = {}

queue = deque()

for i in range(max_x):
    for j in range(max_y):
        distance[f"{i}_{j}"] = INFINITE_DIST
        prev[f"{i}_{j}"] = None
        queue.append(f"{i}_{j}")
distance[start_index] = 0


while queue:
    u = find_min(queue)
    # print(u[0])
    value = queue.remove(u)
    indices = u.split("_")
    x = int(indices[0])
    y = int(indices[1])
    neighbours = [f"{x}_{y-1}", f"{x}_{y+1}",
                  f"{x-1}_{y}", f"{x+1}_{y}"]

    for v in neighbours:
        if v in queue:
            alt = distance[u] + calculate_distance(u, v)
            if alt < distance[v]:
                distance[v] = alt
                prev[v] = u

# print(distance)
# print(prev)

path_queue = deque()

u = end_index
if prev[u] != None or prev[u] == start_index:
    try:
        while u:
            path_queue.appendleft(u)
            u = prev[u]
    except:
        pass

print(path_queue)
print(len(path_queue)-1)
