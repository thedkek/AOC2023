
def calc(_l: list) -> int:
    total = 0

    while not all(x == 0 for x in _l):
        total += _l[-1]
        _l = [t - _l[idx] for idx, t in enumerate(_l[1:])]

    return total


def part_one():
    _result = 0

    for line in lines:
        _l = list(map(int, line.split(" ")))
        _result += calc(_l)
    
    print(f"Part one: {_result}")
    

def part_two():
    _result = 0

    for line in lines:
        _l = list(map(int, reversed(line.split(" "))))
        _result += calc(_l)
           
    print(f"Part two: {_result}")

    
with open("Day9\input.txt") as f:
    lines = f.read().splitlines()
    part_one()
    part_two()
