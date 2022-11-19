def diamond(row, item):
    for loop1 in range(int(item)):
        half = int(row) / 2
        x = int(1)
        y = int(half)
        print("")
        for loop in range(1,int(row)+1 ,1):
            if loop < half:
                print(("    " * y) + (" X " * x))
                x += 2
                y -= 1
            else:
                print(("    " * y) + (" X " * x))
                x -= 2
                y += 1

def inputnum():
    row = input("Enter number of rows : ")
    item = input("How many diamonds do you want : ")

    if row.isdigit() and item.isdigit():
        diamond(row, item)
    else:
        print("----------------------")
        print("            | Try again |")
        print("Please enter only number!!!")
        print("----------------------")
        return inputnum()

inputnum()