f = open("day10_input.txt", "r")

X = 1
cycle_count = 0
signal_strenght = {}
signal_change = 0

total_signal = 0

actions = []

for line in f:
    if line.startswith("noop"):
        actions.append("noop")
    elif line.startswith("addx"):
        actions.append("noop")
        actions.append(line)
f.close()


for instruction in actions:
    cycle_count += 1
    if (cycle_count - 20) % 40 == 0:
        signal_strenght["cycle " + str(cycle_count) + " register"] = X
        total_signal += X * cycle_count
        signal_strenght["cycle " +
                        str(cycle_count) + " signal"] = X * cycle_count

    if instruction.startswith("noop"):
        pass
    elif instruction.startswith("addx"):
        content = instruction.split()
        signal_change = int(content[1])
        X += signal_change


print(X)
print(signal_strenght)
print(total_signal)
