
import re


with open("Day4\input.txt", "r") as f:
    lines = f.readlines()


def part_one():
    total = 0

    for l in lines:
        id, w_nums, _nums = re.split(r": | \| ", l.strip())

        w_nums = re.split(" ", w_nums)
        w_nums = list(filter(None, w_nums))

        _nums = re.split(" ", _nums)
        _nums = list(filter(None, _nums))

        m = [n for n in _nums if n in w_nums]

        if m:
            total += 2**(len(m)-1)

    print(total)

part_one()
