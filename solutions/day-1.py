left_column_d = []
right_column_d = []

left_column_s = []
right_column_s = []

with open('input.txt', 'r') as file:
    data = file.read()

    lines = data.splitlines()
    for line in lines:
        left, right = line.split()

        left_column_d.append(int(left))
        right_column_d.append(int(right))

        left_column_s.append(int(left))
        right_column_s.append(int(right))


# Part 1

total = 0

for i in range(len(left_column_d)):
    smallest_left = min(left_column_d)
    smallest_right = min(right_column_d)

    total += abs(smallest_left - smallest_right)

    # print(f"{smallest_left} - {smallest_right} = {abs(smallest_left - smallest_right)}")

    left_column_d.remove(smallest_left)
    right_column_d.remove(smallest_right)

print("Total Difference:", total)


# Part 2

similarity = 0

for i in range(len(left_column_s)):
    current_left = left_column_s[i]

    count_right = right_column_s.count(current_left)

    similarity += (count_right * current_left)

print("Total Similarity:", similarity)
