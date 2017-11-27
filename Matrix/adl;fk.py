def accept_num():
    sIn = str(input("Numbers"))
    return sIn
def reverse(x):
    reversed = str(x)[::-1]
    return reversed

def check_palindrome(x,y):
    pal = 0
    if str(x) == str(y):
        pal = 1
    return pal
def addnum(x,y):
    new =  int(x) + int(y)
    return new

user = accept_num()
r1 = reverse(user)
check = 0
new = ""
while True:
    if check >= 500:
        print("Never palendrome")
        break
    if check == 0:
        if check_palindrome(user, r1) == 1:
            print("plandrome after {0} with {1}".format(check, user))
            break

        else:
            new = addnum(user, r1)
    else:
        if check_palindrome(new, reverse(new)) == 1:
            print("plandrome after {0} with {1}".format(check, new))
            break
        else:
            new = addnum(new, reverse(new))


    check += 1
    print("check: {0}".format(check))