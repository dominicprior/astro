image = [
    [2, 2, 2, 2],
    [2, 2, 0, 2],
    [2, 0, 0, 2],
    [2, 2, 2, 2]
]

WHITE, RED, BLUE = 0, 1, 3

stack = [(1, 2)]

while stack:
    r, c = stack.pop(0)
    image[r][c] = RED
    for (x,y) in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
        if image[x][y] == WHITE:
            stack.append((x, y))
            image[x][y] = BLUE

for row in image:
    print(row)
