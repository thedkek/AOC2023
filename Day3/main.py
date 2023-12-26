import re, string

with open("Day3\input.txt", "r") as f:
    lines = f.readlines()

def part_one():
    total = 0

    punctuations = "\\".join(string.punctuation.replace(".", ""))
    pattern = f"[{punctuations}]"
    
    for row, l in enumerate(lines):
        matches = re.finditer(r'\d+', l)
        for m in matches:
            start = m.start() - 1 if m.start() -1  > 0 else 0
            end = m.end() + 1 if m.end() < len(l) - 1 else len(l) - 1

            above = lines[row - 1][start:end] if row > 0 else None
            below = lines[row + 1][start:end] if row < len(lines) - 1 else None

            if re.search(pattern, l[start:end]):
                total += int(m.group(0))
            elif above and re.search(pattern, above):
                total += int(m.group(0))
            elif below and re.search(pattern, below):
                total += int(m.group(0))

    print(total)

def part_two():
    total = 0
    pattern = r"\*"
    for row, l in enumerate(lines):
        matches = re.finditer(pattern, l)
        for m in matches:
            idx = m.start()

            start = idx - 3
            end = idx + 4

            above = lines[row - 1][start:end] if row > 0 else None
            below = lines[row + 1][start:end] if row < len(lines) - 1 else None

            if _ := re.match(r"(\d+)\*(\d+)", l[start:end]):
                total += int(_.group(1)) * int(_.group(2))
            elif _ := re.finditer(r"\d+", above):
                if row == 99:
                    for x in _:
                        print(x)


# part_one()
part_two()
