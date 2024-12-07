with open('input.txt', 'r') as file: data = file.read()

grid = [list(row) for row in data.splitlines()]
rows, cols = len(grid), len(grid[0])

# directions [up, right, down, left]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_symbols = ['^', '>', 'v', '<']

start_position = None

for r in range(rows):
    for c in range(cols):
        if grid[r][c] in direction_symbols:
            guard_position = (r, c)
            guard_direction = direction_symbols.index(grid[r][c])
            grid[r][c] = '.' # clear start position
            break
start_position = guard_position
start_direction = guard_direction

# track all of the visited positions
visited = set()
visited.add(guard_position)


# part 1
while True:
    r, c = guard_position
    dr, dc = directions[guard_direction]
    next_r, next_c = r + dr, c + dc

    # verify guard is not out of bounds
    if not (0 <= next_r < rows and 0 <= next_c < cols):
        break

    # check if next position is a wall
    if grid[next_r][next_c] == '#':
        # turn clockwise
        guard_direction = (guard_direction + 1) % 4
        continue
    else:
        # move guard
        guard_position = (next_r, next_c)
        visited.add(guard_position)

print("Part 1:", len(visited))


# part 2
def simulate_movement(start_position, start_direction):
    rows, cols = len(grid), len(grid[0])
    visited_states = set()
    
    position = start_position
    direction = start_direction

    while True:
        state = (position, direction)
        if state in visited_states:
            return True
        visited_states.add(state)

        r, c = position
        dr, dc = directions[direction]
        next_r, next_c = r + dr, c + dc

        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        if grid[next_r][next_c] == '#':
            direction = (direction + 1) % 4
        else:
            position = (next_r, next_c)

    return False


rows, cols = len(grid), len(grid[0])
valid_positions = 0

for r in range(rows):
    for c in range(cols):
        if (r, c) != start_position and grid[r][c] == '.':
            grid[r][c] = '#'
            if simulate_movement(start_position, start_direction):
                valid_positions += 1
            grid[r][c] = '.'



print("Part 2:", valid_positions)