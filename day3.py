f = open("day3_input.txt", "r")

sum_chars = 0

for line in f:
    line = line.strip()
    middle = int(len(line) / 2)
    first_half = set(line[0:middle])
    second_half = set(line[middle:])

    inter = first_half.intersection(second_half)
    for e in inter:
        char_num = ord(e)
        if char_num >= 97:
            sum_chars += char_num - 96
        else:
            sum_chars += char_num - 38

f.close()

f = open("day3_input.txt", "r")

sum_chars2 = 0
line_cnt = 0
res_list = []

for line in f:
    line = line.strip()
    print(line)
    res_list.append(set(line))

    line_cnt += 1

    if line_cnt == 3:
        line_cnt = 0

        inter = set.intersection(*res_list)
        print(inter)
        for e in inter:
            char_num = ord(e)
            if char_num >= 97:
                sum_chars2 += char_num - 96
            else:
                sum_chars2 += char_num - 38

        res_list = []


print(sum_chars2)

f.close()
