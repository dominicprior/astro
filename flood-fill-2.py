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
    if image[r][c] == WHITE:
        image[r][c] = RED

        stack.append((r + 1, c))
        stack.append((r - 1, c))
        stack.append((r, c + 1))
        stack.append((r, c - 1))

for row in image:
    print(row)
