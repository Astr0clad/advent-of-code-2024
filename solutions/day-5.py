with open('input.txt', 'r') as file: data = file.read()

rules_section, updates_section = data.split("\n\n")
    
# Parse rules
rules = []
for line in rules_section.splitlines():
    x, y = map(int, line.split('|'))
    rules.append((x, y))

# Parse updates
updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
  
# Part 1

def is_valid_update(update):
    position = {page: index for index, page in enumerate(update)}

    for x, y in rules:
        if x in position and y in position:
            if position[x] >= position[y]:
                return False
    return True


# Part 2
def fix_update(update):
    update = update[:]
    changed = True

    while changed:
        changed = False

        for x,y in rules:
            if x in update and y in update:
                ix, iy = update.index(x), update.index(y)

                if ix > iy:
                    update[ix], update[iy] = update[iy], update[ix]
                    changed = True
    return update


# run it all here because it is easier
valid_middle_pages = []
corrected_middle_pages = []

for update in updates:
    if is_valid_update(update):
        middle_page = update[len(update) // 2]
        valid_middle_pages.append(middle_page)
    else:
        corrected = fix_update(update)
        middle_page = corrected[len(corrected) // 2]
        corrected_middle_pages.append(middle_page)

print("Part 1:", sum(valid_middle_pages))
print("Part 2:", sum(corrected_middle_pages))