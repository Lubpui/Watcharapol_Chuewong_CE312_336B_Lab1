row = int(input("Enter number of rows : "))
half = row/2
x = 1
y = int(half)

for loop in range(1, row+1, 1):
    if loop < half:
        print(("    "*y)+(" X "*x))
        x += 2
        y -= 1
    else:
        print(("    " * y) + (" X " * x))
        x -= 2
        y += 1

