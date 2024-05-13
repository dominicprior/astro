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

    if image[r+1][c] == WHITE:
        stack.append((r + 1, c))
        image[r+1][c] = BLUE
    if image[r-1][c] == WHITE:
        stack.append((r - 1, c))
        image[r-1][c] = BLUE
    if image[r][c+1] == WHITE:
        stack.append((r, c + 1))
        image[r][c+1] = BLUE
    if image[r][c-1] == WHITE:
        stack.append((r, c - 1))
        image[r][c-1] = BLUE

for row in image:
    print(row)
