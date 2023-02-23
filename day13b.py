import itertools
import functools


def read_input():
    f = open("day13_input.txt", "r")
    array = []
    for line in f:
        line = line.strip()
        if line != '':
            array.append(eval(line))
    f.close()
    return array


def compare_items(item_left, item_right):
    if item_left is None:
        return -1
    if item_right is None:
        return 1

    if isinstance(item_left, int) and isinstance(item_right, int):
        if item_left < item_right:
            return -1
        elif item_left > item_right:
            return 1
        else:
            return 0
    elif isinstance(item_left, list) and isinstance(item_right, list):
        for it_l, it_r in itertools.zip_longest(item_left, item_right):
            if (result := compare_items(it_l, it_r)) != 0:
                return result
        return 0
    else:
        it_l = [item_left] if isinstance(item_left, int) else item_left
        it_r = [item_right] if isinstance(item_right, int) else item_right
        return compare_items(it_l, it_r)


input = read_input()
sum_indices = 0
output = []
for i in range(0, len(input), 2):
    print(i)
    result = compare_items(input[i], input[i+1])
    current_index = int((i + 1) / 2 + 1)
    if result == -1:
        sum_indices += current_index
    print(f"index: {current_index} result: {result}")
    # print(f"left: {input[i]} right: {input[i+1]} result: {result}")

print(f"sum: {sum_indices}")

div1, div2 = [[2]], [[6]]
sorted_input = sorted([*input, div1, div2],
                      key=functools.cmp_to_key(compare_items))
print(sorted_input)
print((sorted_input.index(div1) + 1) * (sorted_input.index(div2) + 1))
