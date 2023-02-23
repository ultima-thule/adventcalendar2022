f = open("day6_input.txt", "r")
result = 0
for line in f:
    for i in range(len(line) - 14):
        s = set([x for x in line[i:i+14]])
        if len(s) == 14:
            result = i + 14
            break

print(result)

f.close()
