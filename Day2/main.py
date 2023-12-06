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


    with open("Day2\input.txt", "r") as f:
        lines = f.readlines()

    for l in lines:
        pass
   
part_one()