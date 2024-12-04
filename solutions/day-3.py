import re

# Part 1

with open('input.txt', 'r') as file:
    data = file.read()
    
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)

    total = 0

    for match in matches:
        total += int(match[0]) * int(match[1])

    print("Pt 1 Total:", total)

    # Part 2

    # regex is pretty neat
    new_pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(new_pattern, data)

    total = 0

    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            a, b = match.split(",")
            a = a.replace("mul(", "")
            b = b.replace(")", "")

            if enabled:
                total += int(a) * int(b)
    
    print("Pt 2 Total:", total)
