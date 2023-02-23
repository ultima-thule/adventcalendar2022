from collections import deque


def read_input():
    f = open("day14_input.txt", "r")
    res = []
    for line in f:
        line = line.strip()
        res.append([tuple(int(i) for i in x.strip().split(','))
                    for x in line.split("->")])
    f.close()
    return res


def mark_x(mapa, start, end, y):
    for x in range(start, end + 1):
        mapa.update({(x, y)})


def mark_y(mapa, start, end, x):
    for y in range(start, end + 1):
        mapa.update({(x, y)})


def draw_map(mapa):
    result = set()

    for line in mapa:
        for i in range(0, len(line) - 1):
            x_start = line[i][0]
            y_start = line[i][1]

            x_end = line[i+1][0]
            y_end = line[i+1][1]

            mark_x(result, min(x_start, x_end),
                   max(x_start, x_end), y_start)

            mark_y(result, min(y_start, y_end),
                   max(y_start, y_end), x_start)
    return result


mapa = read_input()
drawn_map = draw_map(mapa)

x, y = (500, 0)
max_y = max((y for x, y in drawn_map))

count = 0
part1 = 0
part2 = 0

while True:
    if (x, y) in drawn_map:
        (x, y) = (500, 0)
    if y > max_y and part1 == 0:
        part1 = count
    if (x, y+1) not in drawn_map and y < max_y + 1:
        y += 1
    elif (x-1, y+1) not in drawn_map and y < max_y + 1:
        y += 1
        x -= 1
    elif (x+1, y+1) not in drawn_map and y < max_y + 1:
        y += 1
        x += 1
    else:
        count += 1
        drawn_map.add((x, y))
    if (x, y) == (500, 0):
        part2 = count
        break

print(drawn_map)
print(count)
print(part1)
print(part2)
