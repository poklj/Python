__author__ = "Zachary Higgs"
def ulam(x):
    """
    To return the number of iterations to make the input number equal to 1 by:
    Dividing by 2 if the current number is even
    or Multiplying by 3 and adding one if the current number is odd

    :param x: Number (int)
    :return: The number of iterations
    """

    iterations = 0

    while x != 1:
        if x%2 == 0:
           x = x/2
        else:
           x = (x*3)+1

        iterations += 1

    return iterations

print(ulam(1337))

numberset = [1337, 45, 1200, 11, 4356]

for i in numberset:
    print("Number {0} is 1 after {1} ulam iterations".format(i, ulam(i)))