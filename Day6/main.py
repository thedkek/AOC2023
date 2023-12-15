import re

with open("Day6/input.txt", "r") as f:
    lines = f.read().splitlines()


def part_one():
    total = 1
    races = list(zip(re.split("\s+", lines[0]), re.split("\s+", lines[1])))

    races.pop(0)

    for r in races:
        result = 0
        time, dist = r

        time = int(time)
        dist = int(dist)

        for t in range(1, time + 1):
            _d = (time - t ) * t

            if _d > dist:
                result += 1

        total *= result

    print(f"part one: {total}")


def part_two():
    time, dist = [re.sub(r"\w+:|\s+", "",lines[0]), re.sub(r"\w+:|\s+", "",lines[1])]

    time = int(time)
    dist = int(dist)

    result = 0

    for t in range(1, time + 1):
        _d = (time - t) * t

        if _d > dist:
            result += 1

    print(f"part two: {result}")

part_one()
part_two()