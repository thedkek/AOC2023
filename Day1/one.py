import re

with open("Day1\input.txt", "r") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        res = re.findall(r"(\d)", line)
        if len(res) > 1:
            total += int(res[0] + res[-1])
        else:
            total += int(res[0] * 2)

    print(total)
