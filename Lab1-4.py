def Harmonic(step,lim):
    step = float(step)
    if step == 0:
        return 0
    else:
        value = 1 / (step +1) + Harmonic(step - 1, lim -1)
        print("Limit = ",lim," , Value = ",value)
        return value

def inputnum():
    step = input("Enter Harmonic step : ")
    lim = int(step)

    if step.isdigit():
        Harmonic(step,lim)
    else:
        print("----------------------")
        print("            | Try again |")
        print("Please enter only number!!!")
        print("----------------------")
        return inputnum()

inputnum()
