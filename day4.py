f = open("day4_input.txt", "r")

full_contain = 0
overlap = 0
for line in f:
    splitted = line.strip().split(",")
    first_line = splitted[0].split("-")
    second_line = splitted[1].split("-")
    first_A = int(first_line[0])
    first_Z = int(first_line[1])
    second_A = int(second_line[0])
    second_Z = int(second_line[1])

    if (first_A >= second_A and first_Z <= second_Z) or (second_A >= first_A and second_Z <= first_Z):
        #print(f"overlap 1: {first_line}, 2: {second_line}")
        full_contain += 1

    if (first_Z >= second_A and first_Z <= second_Z) or (second_Z >= first_A and second_Z <= first_Z):
        print(f"overlap 1: {first_line}, 2: {second_line}")
        overlap += 1


print(overlap)

f.close()
