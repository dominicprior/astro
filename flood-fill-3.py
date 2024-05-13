image = [
    [2, 2, 2, 2],
    [2, 2, 0, 2],
    [2, 0, 0, 2],
    [2, 2, 2, 2]
]

WHITE, RED, BLUE = 0, 1, 3

stack = [(1, 2)]

def explore(r,c):
    if image[r][c] == WHITE:
        stack.append((r, c))
        image[r][c] = BLUE

while stack:
    r, c = stack.pop(0)
    image[r][c] = RED
    explore(r+1,c)
    explore(r-1,c)
    explore(r,c+1)
    explore(r,c-1)

for row in image:
    print(row)

