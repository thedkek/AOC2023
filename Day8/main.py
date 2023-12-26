import math
import re


with open("Day8\input.txt", "r") as f:
    lines = f.read().splitlines()


instructions = re.findall(r"\w", lines[0])
nodes = lines[2:]


def part_one():
    r = re.compile("AAA =")

    current_node = re.findall(r"(\w+)", list(filter(r.match, nodes))[0])

    steps = 0

    while current_node[0] != ("ZZZ"):
        for i in instructions:
            if i == 'L':
                r = re.compile(current_node[1] + " =")
            else:
                r = re.compile(current_node[2] + " =")

            _n = list(filter(r.match, nodes))[0]
            
            current_node = re.findall(r"(\w+)", _n)

            steps += 1

    print(steps)


def part_two():
    r = re.compile("\w{2}A =")

    current_nodes = []

    for node in list(filter(r.match, nodes)):
        _n = re.findall(r"(\w{3})", node)
        current_nodes.append(_n)

    print(current_nodes)

    steps = [0 for _ in current_nodes]


    for idx, current_node in enumerate(current_nodes):
        while not current_node[0].endswith("Z"):
            for i in instructions:
                if i == 'L':
                    r = re.compile(current_node[1] + " =")
                else:
                    r = re.compile(current_node[2] + " =")

                _n = list(filter(r.match, nodes))[0]
                
                current_node = re.findall(r"(\w+)", _n)

                steps[idx] += 1
        print(steps)

    print(math.lcm(*steps))


part_one()
part_two()