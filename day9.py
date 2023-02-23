class Position:
    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def signum(value):
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0


def move_tail(positions_list, direction, count):

    for i in range(count):
        for pos in range(9):
            head = positions_list[pos]
            tail = positions_list[pos + 1]

            if (pos == 0):
                if direction == 'L':
                    head.x -= 1
                elif direction == 'R':
                    head.x += 1
                elif direction == 'U':
                    head.y += 1
                elif direction == 'D':
                    head.y -= 1

            diff_x = head.x - tail.x
            diff_y = head.y - tail.y

            print(
                f"Pos: {pos}, count: {count}, head {head.x}, {head.y} tail: {tail.x}, {tail.y}")

            if abs(diff_x) == 2:
                tail.x += signum(diff_x) * 1
                if head.y != tail.y:
                    tail.y += signum(diff_y) * 1

            if abs(diff_y) == 2:
                tail.y += signum(diff_y) * 1
                if head.x != tail.x:
                    tail.x += signum(diff_x) * 1

        positions.add(str(positions_list[9].x) +
                      "-" + str(positions_list[9].y))


positions = set()

positions_list = []
for i in range(10):
    positions_list.append(Position(0, 0))

f = open("day9b_input.txt", "r")
for line in f:
    cmd = line.strip().split()

    move_tail(positions_list, cmd[0], int(cmd[1]))

    print(
        f"Head: {positions_list[0].x}, {positions_list[0].y}, tail: {positions_list[9].x}, {positions_list[9].y}")
f.close()

print(len(positions))


# print(current_position_head)
# print(current_position_tail)
