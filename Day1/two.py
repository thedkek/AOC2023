import re


with open("Day1\input.txt", "r") as f:
    lines = f.readlines()

    d = ["",
         "one",
         "two",
         "three",
         "four",
         "five",
         "six",
         "seven",
         "eight",
         "nine"
         ]

    total = 0

    for line in lines:
        res = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        d1 = res[0] if res[0].isnumeric() else str(d.index(res[0]))
        d2 = res[-1] if res[-1].isnumeric() else str(d.index(res[-1]))

        total += int(d1 + d2)

    print(total)