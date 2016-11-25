

def calc():
    v, l = input().strip()

    child_count = {}
    parent_dict = {}

    for _ in range(v):
        input_value = input().strip().split()
        node1, node2 = int(input_value[0]), int(input_value[1])

        if node2 in child_count:
            child_count[node2] += 1
        else:
            child_count[node2] = 1

        parent = node2

        while parent in parent_dict:
            par = parent_dict[parent]
            child_count[par] += 1
            parent = par

        parent_dict[node1] = node2

    print(len(list(filter(lambda k: k[1] % 2 == 1, child_count.items()))) - 1)