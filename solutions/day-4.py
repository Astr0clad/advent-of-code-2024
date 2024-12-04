data = None

with open('input.txt', 'r') as file: data = file.read()

pt1 = 0
pt2 = 0

G = data.split('\n')
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        # Check for "XMAS" horizontally
        if c+3<C and G[r][c]=='X' and G[r][c+1]=='M' and G[r][c+2]=='A' and G[r][c+3]=='S':
            pt1 += 1
        # Check for "XMAS" diagonally down-right
        if r+3<R and c+3<C and G[r][c]=='X' and G[r+1][c+1]=='M' and G[r+2][c+2]=='A' and G[r+3][c+3]=='S':
            pt1 += 1
        # Check for "SAMX" vertically down
        if r+3<R and G[r][c]=='S' and G[r+1][c]=='A' and G[r+2][c]=='M' and G[r+3][c]=='X':
            pt1 += 1
        # Check for "XMAS" vertically down
        if r+3<R and G[r][c]=='X' and G[r+1][c]=='M' and G[r+2][c]=='A' and G[r+3][c]=='S':
            pt1 += 1
        # Check for "SAMX" horizontally
        if c+3<C and G[r][c]=='S' and G[r][c+1]=='A' and G[r][c+2]=='M' and G[r][c+3]=='X':
            pt1 += 1
        # Check for "SAMX" diagonally down-right
        if r+3<R and c+3<C and G[r][c]=='S' and G[r+1][c+1]=='A' and G[r+2][c+2]=='M' and G[r+3][c+3]=='X':
            pt1 += 1
        # Check for "SAMX" diagonally up-right
        if r-3>=0 and c+3<C and G[r][c]=='S' and G[r-1][c+1]=='A' and G[r-2][c+2]=='M' and G[r-3][c+3]=='X':
            pt1 += 1
        # Check for "XMAS" diagonally up-right
        if r-3>=0 and c+3<C and G[r][c]=='X' and G[r-1][c+1]=='M' and G[r-2][c+2]=='A' and G[r-3][c+3]=='S':
            pt1 += 1

        # Check for "MAS" in a 3x3 square pattern for pt2
        if r+2<R and c+2<C and G[r][c]=='M' and G[r+1][c+1]=='A' and G[r+2][c+2]=='S' and G[r+2][c]=='M' and G[r][c+2]=='S':
            pt2 += 1
        # Check for "SAM" in a 3x3 square pattern for pt2
        if r+2<R and c+2<C and G[r][c]=='S' and G[r+1][c+1]=='A' and G[r+2][c+2]=='M' and G[r+2][c]=='S' and G[r][c+2]=='M':
            pt2 += 1
        # Check for "MAS" in a 3x3 square pattern for pt2
        if r+2<R and c+2<C and G[r][c]=='M' and G[r+1][c+1]=='A' and G[r+2][c+2]=='S' and G[r+2][c]=='S' and G[r][c+2]=='M':
            pt2 += 1
        # Check for "SAM" in a 3x3 square pattern for pt2
        if r+2<R and c+2<C and G[r][c]=='S' and G[r+1][c+1]=='A' and G[r+2][c+2]=='M' and G[r+2][c]=='M' and G[r][c+2]=='S':
            pt2 += 1


print(f'Pt 1: XMAS found {pt1} times')
print(f'Pt 2: X-MAS found {pt2} times')