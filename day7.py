class TreeNode (object):
    def __init__(self) -> None:
        self.name = None
        self.nodes = []
        self.own_size = 0
        self.total_size = 0
        self.prev_node = None
        self.is_file = False

    def next(self, child_no):
        return self.nodes[child_no]

    def prev(self):
        if self.prev_node == None:
            return self
        return self.prev_node

    def goto(self, node_name):
        # if self.name == node_name:
        #    return self
        for child in self.nodes:
            if child.name == node_name:
                return child
        return None

    def add(self, node_name, is_file=False, file_size=0):
        node = TreeNode()
        node.name = node_name
        node.is_file = is_file
        node.own_size = file_size
        node.prev_node = self
        self.nodes.append(node)
        return node

    def increase_size(self, size_to_add):
        if self.is_file == False:
            self.own_size += size_to_add
        if self.prev_node is not None:
            self.prev_node.increase_size(size_to_add)

    def print(self, level_no):
        intend = level_no*3
        print(
            " ".join([intend * '-', self.name, str(self.own_size).rjust(100 - intend - len(self.name))]))

        for node in self.nodes:
            node.print(level_no + 1)

    def iter_sizes(self, ret_list):
        if not self.is_file:
            #print(f"{self.name} {self.own_size}")
            if self.own_size <= 100000:
                ret_list.append(int(self.own_size))

        for node in self.nodes:
            node.iter_sizes(ret_list)

    def iter_sizes_update(self, ret_list, needed_size):
        if not self.is_file:
            #print(f"{self.name} {self.own_size}")
            if self.own_size >= needed_size:
                ret_list.append(int(self.own_size))

        for node in self.nodes:
            node.iter_sizes_update(ret_list, needed_size)


f = open("day7_input.txt", "r")

tree = TreeNode()
tree.name = "/"
total_sizes = 0

current_node = tree

for line in f:
    cmd = line.split()

    # zmiana katalogu
    if line.startswith("$ cd "):
        old = current_node.name
        dir_name = cmd[2]

        # wyjdź poziom wyżej
        if dir_name == "..":
            current_node = current_node.prev()
            #print(f"katalog zmieniony na {current_node.name}")
            continue

        # wyjdź do roota
        if dir_name == "/":
            current_node = tree
            #print(f"katalog zmieniony na {current_node.name}")
            continue

        # przejdź do podkatalogu
        node = current_node.goto(dir_name)
        if node is not None:
            current_node = node
            #print(f"katalog zmieniony na {current_node.name}")

    # zawartość - katalog
    elif line.startswith("dir"):
        dir_name = cmd[1]

        #print(f"dodanie katalogu {dir_name}")
        current_node.add(dir_name, False)

    # zawartosc - plik
    elif cmd[0].isnumeric():
        file_name = cmd[1]
        file_size = int(cmd[0])

        #print(f"dodanie pliku {file_name}")
        current_node.add(file_name, True, file_size)
        current_node.increase_size(file_size)

# tree.print(1)

# print(tree.total_size)

return_list = []
tree.iter_sizes(return_list)

result = 0
for i in return_list:
    result += i

print(result)

space_total = 70000000
space_for_update = 30000000
space_available = 70000000 - tree.own_size
space_missing = space_for_update - space_available

print(
    f"available: {space_available}, used: {tree.own_size}, missing for update: {space_missing}")

ret_list_update = []
tree.iter_sizes_update(ret_list_update, space_missing)
min = space_total
for i in ret_list_update:
    if i < min:
        min = i

print(min)


f.close()
