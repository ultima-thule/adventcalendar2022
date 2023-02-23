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
        actions.append(line.strip())
f.close()

line_to_print = ""

for instruction in actions:
    cycle_count += 1
    mod_cycle_count = cycle_count % 40

    if mod_cycle_count == 1:
        print(line_to_print)
        line_to_print = ""

    if X == mod_cycle_count-1 or X-1 == mod_cycle_count-1 or X+1 == mod_cycle_count-1:
        line_to_print += "#"
    else:
        line_to_print += "."

    if instruction.startswith("noop"):
        pass

    if instruction.startswith("addx"):
        content = instruction.split()
        signal_change = int(content[1])
        X += signal_change

print(line_to_print)
