reports = []

with open('input.txt', 'r') as file:
    data = file.read()

    lines = data.splitlines()
    for line in lines:
        levels = line.split()
        reports.append(levels)


# Part 1

total_safe = 0

for report in reports:

    valid = False
    
    is_ascending = all(int(report[i]) <= int(report[i + 1]) for i in range(len(report) - 1))
    is_descending = all(int(report[i]) >= int(report[i + 1]) for i in range(len(report) - 1))

    
    if is_ascending:
        valid = all(1 <= int(report[i + 1]) - int(report[i]) <= 3 for i in range(len(report) - 1))
    elif is_descending:
        valid = all(1 <= int(report[i]) - int(report[i + 1]) <= 3 for i in range(len(report) - 1))

    if valid:
        total_safe += 1
        
print("Pt 1 Total Safe:", total_safe)


# Part 2

def is_safe(report):
    valid = False

    is_ascending = all(int(report[i]) <= int(report[i + 1]) for i in range(len(report) - 1))
    is_descending = all(int(report[i]) >= int(report[i + 1]) for i in range(len(report) - 1))
    
    if is_ascending:
        valid = all(1 <= int(report[i + 1]) - int(report[i]) <= 3 for i in range(len(report) - 1))
    elif is_descending:
        valid = all(1 <= int(report[i]) - int(report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    return valid

def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False

safe_with_dampener = sum(is_safe_with_dampener(report) for report in reports)

print("Pt 2 Total Safe:", safe_with_dampener)
