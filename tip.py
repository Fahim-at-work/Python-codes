def TakeInput():
    
    total_bill = float(input("Enter the total bill amount: "))
    number_of_people = int(input("Enter the number of people you want to split the bill: "))
    return total_bill, number_of_people


def CalculatorTip(x, y):
    """
    :param y: int
    :type x: float
    """
    tip_amount = 0.13 * x
    individual_tip = tip_amount / y
    return tip_amount, individual_tip


def ShowOutput(d, f):
    print("Total tip {0:.2f}".format(d))
    print("Individual tip {0:.2f}".format(f))


def main():
    a, b = TakeInput()
    c, d = CalculatorTip(a, b)
    ShowOutput(c, d)


main()
