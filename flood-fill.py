def flood_fill(image, x, y, new_color):
    
    old_color = image[x][y]  # this could be implied
    ####################
    stack = [(x, y)]
    
    while stack:
        r, c = stack.pop(0)
        if image[r][c] == old_color:
            image[r][c] = new_color

            stack.append((r + 1, c))
            stack.append((r - 1, c))
            stack.append((r, c + 1))
            stack.append((r, c - 1))
    ####################
    return image

image = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]
x, y = 1, 2
new_color = 2
print("Original Image:")
for row in image:
    print(row)

filled_image = flood_fill(image, x, y, new_color)
print("\nFlood Filled Image:")
for row in filled_image:
    print(row)
