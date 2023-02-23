f = open("day5_input.txt", "r")

queues = []
for line in f:
    if line[0] == "[":
        # read row
        local_list = []
        for i in range(0, int(len(line) / 4)):
            item = line[i * 4 + 1:i * 4 + 2]
            local_list.append(item)

        # initialize matrix
        if len(queues) == 0:
            for n in local_list:
                queues.append([])

        # reverse and create matrix
        for i in range(0, len(local_list)):
            if local_list[i] != " ":
                queues[i].insert(0, local_list[i])
    elif line[0] == " ":
        pass
    elif line[0] == "m":
        orders = line.strip().split()
        how_many = int(orders[1])
        from_queue = int(orders[3]) - 1
        to_queue = int(orders[5]) - 1

        #print(f"From {from_queue} to {to_queue} that many {how_many}")

        # move items
        # print("before")
        # print(queues[from_queue])
        # print(queues[to_queue])
        items = queues[from_queue][-how_many:]
        queues[from_queue] = queues[from_queue][0:-how_many]
        # print(items)
        queues[to_queue].extend(items)
        # queues[to_queue].append(item)
        # print("after")
        # print(queues[from_queue])
        # print(queues[to_queue])

result = ""
for q in queues:
    result = result + q[-1]

print(result)

f.close()
