class Blueprint():
    def __init__(self) -> None:
        self.number = 0
        self.costs = {"ore_ore": 0, "clay_ore": 0, "obsidian_ore": 0,
                      "obsidian_clay": 0, "geode_ore": 0, "geode_obsidian": 0}

        self.robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}

        self.goods = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}

        self.mutex = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}

    def _produce_good(self, what_good):
        if self.robots[what_good] > 0:
            print(f"produce {what_good}")
            self.goods[what_good] += self.robots[what_good]

    def _produce_ore_robot(self, start=True):
        if start and self.mutex["ore"] == 0:
            if self.goods["ore"] >= self.costs["ore_ore"]:
                print("start produce ore robot")
                self.mutex["ore"] = 1
                self.goods["ore"] -= self.costs["ore_ore"]
        elif not start and self.mutex["ore"] == 1:
            print("end produce ore robot")
            self.mutex["ore"] = 0
            self.robots["ore"] += 1

    def _produce_clay_robot(self, start=True):
        if start and self.mutex["clay"] == 0:
            if self.goods["ore"] >= self.costs["clay_ore"]:
                print("start produce clay robot")
                self.mutex["clay"] = 1
                self.goods["ore"] -= self.costs["clay_ore"]
        elif not start and self.mutex["clay"] == 1:
            print("end produce clay robot")
            self.mutex["clay"] = 0
            self.robots["clay"] += 1

    def _produce_obsidian_robot(self, start=True):
        if start and self.mutex["obsidian"] == 0:
            if self.goods["clay"] >= self.costs["obsidian_clay"] and self.goods["ore"] >= self.costs["obsidian_ore"]:
                print("start produce obsidian robot")
                self.mutex["obsidian"] = 1
                self.goods["clay"] -= self.costs["obsidian_clay"]
                self.goods["ore"] -= self.costs["obsidian_ore"]
        elif not start and self.mutex["obsidian"] == 1:
            print("end produce obsidian robot")
            self.mutex["obsidian"] = 0
            self.robots["obsidian"] += 1

    def _produce_geode_robot(self, start=True):
        if start and self.mutex["geode"] == 0:
            if self.goods["obsidian"] >= self.costs["geode_obsidian"] and self.goods["ore"] >= self.costs["geode_ore"]:
                print("start produce geode robot")
                self.mutex["geode"] = 1
                self.goods["obsidian"] -= self.costs["geode_obsidian"]
                self.goods["ore"] -= self.costs["geode_ore"]
        elif not start and self.mutex["geode"] == 1:
            print("end produce geode robot")
            self.mutex["geode"] = 0
            self.robots["geode"] += 1

    def produce(self):
        self._produce_geode_robot(True)
        self._produce_obsidian_robot(True)
        self._produce_clay_robot(True)
        self._produce_ore_robot(True)

        self._produce_good("ore")
        self._produce_good("clay")
        self._produce_good("obsidian")
        self._produce_good("geode")

        self._produce_geode_robot(False)
        self._produce_obsidian_robot(False)
        self._produce_clay_robot(False)
        self._produce_ore_robot(False)

    def print_stats(self, round):
        print(
            f"B-{self.number} #{round} Robots: Ore {self.robots['ore']} Clay {self.robots['clay']} Obsidian {self.robots['obsidian']} Geode {self.robots['geode']}")
        print(
            f"B-{self.number} #{round} Goods: Ore {self.goods['ore']} Clay {self.goods['clay']} Obsidian {self.goods['obsidian']} Geode {self.goods['geode']}\n")


def read_input():
    f = open("day19b_input.txt", "r")
    ret = []

    for line in f:
        line = line.strip().split()

        blueprint = Blueprint()

        blueprint.number = int(line[1].replace(":", ""))
        blueprint.costs["ore_ore"] = int(line[6])
        blueprint.costs["clay_ore"] = int(line[12])
        blueprint.costs["obsidian_ore"] = int(line[18])
        blueprint.costs["obsidian_clay"] = int(line[21])
        blueprint.costs["geode_ore"] = int(line[27])
        blueprint.costs["geode_obsidian"] = int(line[30])

        ret.append(blueprint)
    f.close()

    return ret


def simulate(blueprint):
    ret = 0
    for i in range(0, 24):
        blueprint.produce()
        blueprint.print_stats(i + 1)

    return ret


blueprints = read_input()
max_no = 0

for i in blueprints:
    max_no = max(simulate(i), max_no)

print(max_no)
