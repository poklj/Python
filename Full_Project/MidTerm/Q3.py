__author__ = "Zachary Higgs"

def Calculate_Sal(SalM, PincY, stIncY, length):
    """
    Calculate the earnings for the entire duration of a contract factoring in:
        Static salary per month
        Percent Increased per Year
        Static Pay Increase per year
    :param SalM: static Salary per Month
    :param PincY: Percent Increased per Year
    :param stIncY: static increase Increased per Year
    :param length: how long of a contract (In Years)
    :return: The amount you make (total) by the end of the length of the contract
    """

    finalSal = 0
    yearly = SalM
    for i in range(length):
        if i == 0:
            finalSal += yearly * 12
        else:
            yearly = yearly + (yearly * (PincY/100)) + stIncY
            finalSal += yearly *12

    return finalSal



def Final(x, y):
    """
    Make things easier to display to show function works (!!!PRINT ONLY FUNC, DOES NOT RETURN!!!)
    :param x: Option 1
    :param y: Option 2
    """
    if x > y:
        print("Option 1 (${0}) is Greater then Option 2(${1})".format(x, y))
    elif x < y:
        print("Option 2 (${0}) is Greater then Option 1(${1})".format(y, x))
    else:
        print("Both options are equal: ${0}".format(x))

x = Calculate_Sal(1820, 4, 60, 10)
y = Calculate_Sal(1820, 1, 120, 10)
Final(x, y)
x = Calculate_Sal(1820, 4, 60, 5)
y = Calculate_Sal(1820, 1, 120, 5)
Final(x, y)