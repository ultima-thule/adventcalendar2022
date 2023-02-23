import math


class Monkey:
    index = 0
    items = []
    operation = ""
    divider = 1
    monkey_index_true = 0
    monkey_index_false = 0
    inspections_count = 0

    def __init__(self) -> None:
        self.index = 0
        self.items = []
        self.operation = ""
        self.divider = 1
        self.monkey_index_true = 0
        self.monkey_index_false = 0
        self.inspections_count = 0

    def __str__(self) -> str:
        return f"Index: {self.index}, insp cnt: {self.inspections_count}, divide by: {self.divider}, items: {self.items}"


def init_monkeys():
    monkeys = []
    current_monkey = None

    f = open("day11_input.txt", "r")

    for line in f:

        line = line.replace(',', '').strip()
        cmd = line.split()
        if line.startswith("Monkey"):
            current_monkey = Monkey()
            current_monkey.index = cmd[1]
        elif line.startswith("Starting"):
            for i in range(2, len(cmd)):
                current_monkey.items.append(int(cmd[i]))
        elif line.startswith("Operation"):
            current_monkey.operation = line[17:]
        elif line.startswith("Test"):
            current_monkey.divider = int(cmd[3])
        elif line.startswith("If true"):
            current_monkey.monkey_index_true = int(cmd[5])
        elif line.startswith("If false"):
            current_monkey.monkey_index_false = int(cmd[5])
            monkeys.append(current_monkey)

    f.close()

    return monkeys


def inspect(old, monkey):
    monkey.inspections_count += 1
    return eval(monkey.operation)


def calc_worry_lvl(current_level):
    return math.floor(current_level / 3)


def test_worry_lvl(current_level, divider):
    return current_level % divider == 0


def throw(original, start, monkey, worry_level):
    monkey.items.append(worry_level)
    # print(f"From monkey {original} item {start} throw to monkey {monkey.index} value {worry_level}")


def run_round(monkeys):
    for i in range(len(monkeys)):
        while monkeys[i].items:
            item = monkeys[i].items.pop(0)
            worry_lvl = inspect(item, monkeys[i])
            worry_lvl = calc_worry_lvl(worry_lvl)

            index = -1
            if test_worry_lvl(worry_lvl, monkeys[i].divider):
                index = monkeys[i].monkey_index_true
            else:
                index = monkeys[i].monkey_index_false
            throw(i, item, monkeys[index], worry_lvl)


def myFunc(item):
    return item.inspections_count


monkeys = init_monkeys()

for monkey in monkeys:
    print(monkey)
print("----------------------------")


for i in range(0, 20):
    run_round(monkeys)

max = 0
max2 = 0
monkeys.sort(key=myFunc, reverse=True)

for monkey in monkeys:
    print(monkey)

print(monkeys[0].inspections_count * monkeys[1].inspections_count)
