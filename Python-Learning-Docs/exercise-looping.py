height = int(input('Enter rhombus height (odd): '))
side = height/2
count = 1
space = int(side)
stars = 1
for x in range(height):
    if x <= 10:
        if count <= side:
            print(" "*space + "*"*stars)
            count += 1
            space -= 1
            stars += 2
            continue
        if count <= height + 1:
            print(" "*space + "*"*stars)
            count += 1
            space += 1
            stars -= 2
    else:
        break