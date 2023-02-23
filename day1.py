filepath = "day1_input.txt"

f = open(filepath, "r")

sums = []
sum_elf = 0

for line in f:
    line = line.strip()
    if not line.isnumeric():
        sums.append(sum_elf)
        sum_elf = 0
    else:
        sum_elf += int(line)
f.close()

sums.sort(reverse=True)
print(sums[0]+sums[1]+sums[2])
