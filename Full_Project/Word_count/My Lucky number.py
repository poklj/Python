__author__ ="Zachary"

import math

print (math.factorial(10))
import random
import itertools

#associations
Letters = "MYLUCKYNUMBER"
Letters = list(set(Letters))


def Associate(u):
    digits = [x for x in range(10)]
    d = {}
    for i in u:
        r = random.choice(digits)
        d[i] = r
        digits.remove(r)
    return d


#compute values of words
def val(d, s):
    """

    :param d: Dict
    :param s: String
    :return:
    """
    v = 0
    for i in s:
        v = 10*v + d[i]

    return v


#my = 10*Associated['M']+Associated['Y']
it = 0
#final test:
while True:
    a= Associate(Letters)
    it += 1
    if (a['U']%2 and val(a, "MY") + (val(a, "LUCKY")*3) == val(a, "NUMBER")  ):
        print("FOUND: {0} after {1}".format(val(a, "NUMBER"), it))


#val('u") is odd and MY + (3 * Lucky) = number
# for perm in itertools.permutations(digits):
#   a= dict(zip(letters,perm))
#

