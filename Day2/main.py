import re

def part_one():
    ids = 0
    bag = {'red': 12, 'green': 13, 'blue': 14}

    with open("Day2\input.txt", "r") as f:
        lines = f.readlines()

    for l in lines:
        _ = re.search(r"Game (\d+): ", l)
        
        id, game = [_.group(1), re.sub(_.group(0), "", l)]

        sets = game.split(";")
        
        try:
            for _set in sets:
                matches = re.findall(r"(\d+) (blue|green|red)", _set)
                for match in matches:
                    if int(match[0]) > bag[match[1]]:
                        raise ValueError
            ids += int(id)
        except ValueError:
            pass

    print(ids)


def part_two():
    total = 0
    with open("Day2\input.txt", "r") as f:
        lines = f.readlines()

    for l in lines:
        r = []
        g = []
        b = []

        matches = re.findall(r"((\d+) (red|green|blue))", l)
        for m in matches:
            if m[2] == 'red':
                r.append(int(m[1]))
            elif m[2] == 'green':
                g.append(int(m[1]))
            else:
                b.append(int(m[1]))
        
        total += max(r) * max(g) * max(b)
    
    print(total)

# part_one()
part_two()