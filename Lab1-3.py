# -------------- Main Function ---------------- #
def main(mValue, OEB, prime):

    #-------- Calculate Prime Number -------#
    primeSet = []
    for i in range(2, int(mValue)+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primeSet.append(i)
    print("\n-----------------------")
    print("Prime Number : ", primeSet)
    print("-----------------------\n")
    # ----------------------------------#

    mValue = int(mValue)
    if OEB.upper() in 'O':
        oddNum(mValue, prime, primeSet)
    elif OEB.upper() in 'E':
        EvenNum(mValue, prime, primeSet)
    elif OEB.upper() in 'B':
        BothNum(mValue, prime, primeSet)

# --------- Condition of "Odd" number ----------- #
def oddNum(mValue, prime, primeSet):
    if prime.upper() in "Y":
        if mValue == 0:
                return
        else:
            oddNum((mValue - 1), prime, primeSet)
            if (mValue % 2) != 0 and mValue in primeSet:
                print(mValue, " is  prime  number")
    else:
        if mValue == 0:
            return 0
        else:
            oddNum((mValue - 1), prime, primeSet)
            if (mValue % 2) != 0:
                if mValue in primeSet:
                    print(mValue, " is  prime  number")
                else:
                    print(mValue, " is  not  prime  number")

# --------- Condition of "Even" Number ----------- #
def EvenNum(mValue, prime, primeSet):
    if prime.upper() in "Y":
        if mValue == 0:
            return 0
        else:
            EvenNum((mValue - 1), prime, primeSet)
            if (mValue % 2) != 1 and mValue in primeSet :
                print(mValue, " is  prime  number")
    else:
        if mValue == 0:
            return 0
        else:
            EvenNum((mValue - 1), prime, primeSet)
            if (mValue % 2) == 0:
                if mValue in primeSet:
                    print(mValue, " is  prime  number")
                else:
                    print(mValue, " is  not  prime  number")

# --------- Condition of "Both" Number ----------- #
def BothNum(mValue, prime, primeSet):
    if prime.upper() in "Y":
        if mValue == 0:
            return 0
        else:
            z = BothNum((mValue - 1), prime, primeSet)
            if mValue in primeSet:
                print(mValue, " is  prime  number")
    else:
        if mValue == 0:
            return 0
        else:
            z = BothNum((mValue - 1), prime, primeSet)
            if mValue in primeSet:
                print(mValue, " is  prime  number")
            else:
                print(mValue, " is  not  prime  number")

# --------- Input function ----------- #
def inputOrder():
    mValue = input("Enter max value : ")
    if mValue.isdigit():
        OEB = input("Select O/E/B (Odd or Even or Both) : ")
        if OEB.upper() in ['O', 'E', 'B']:
            Prime = input("Want to select only prime number? (Y/N) : ")
            if Prime.upper() in ['Y', 'N']:
                return main(mValue, OEB, Prime)
            else:   # primeNum
                print("----------------------")
                print("            | Try again |")
                print("Please enter only (Y/N) !!!")
                print("----------------------")
                return inputOrder()
        else:   # OEB
            print("----------------------")
            print("            | Try again |")
            print("Please enter only O/E/B !!!")
            print("----------------------")
            return inputOrder()
    else:   # mValue
        print("----------------------")
        print("            | Try again |")
        print("Please enter only number!!!")
        print("----------------------")
        return inputOrder()
inputOrder()