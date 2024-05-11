image = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]

x, y = 1, 2
new_color = 2
old_color = image[x][y]

stack = [(x, y)]

while stack:
    r, c = stack.pop(0)
    if image[r][c] == old_color:
        image[r][c] = new_color

        stack.append((r + 1, c))
        stack.append((r - 1, c))
        stack.append((r, c + 1))
        stack.append((r, c - 1))

for row in image:
    print(row)
