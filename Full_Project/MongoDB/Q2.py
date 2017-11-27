import MongoDB.Mongo as mong
from pprint import pprint

# [35%] Are the older people more grumpy?
# Print the average scores given by users of age N or over, and those below N,  where N takes values, 30, 40, 45, 50.
# Any comments?

def grabUsers():
    """

    :return:
    """
    userlist = []

    for i in users.find({}):
        userlist.append(i)

    return userlist

def userSplit(nAge, userlist):
    """
    Split the users based on the nAge
    :param nAge: the age to split by
    :param userlist: Userlist
    :return:
    """
    upper = []
    lower = []
    for i in userlist:
        if (i.get('age') >= nAge):
            upper.append(i)
        elif (i.get('age') <= nAge):
            lower.append(i)
    compiledList = []
    compiledList.append(upper)
    compiledList.append(lower)

    return compiledList



if __name__ == '__main__':
    Data = mong.Data()  # Connect
    db = Data.Database  # Pull the Database

    # Setup Collections for Join
    movies = db.movies
    ratings = db.ratings
    users = db.users

    userL = grabUsers()
    # pprint(userL)
    splitCompile = userSplit(50, userL)

    upper = splitCompile[0]
    lower = splitCompile[1]

    # print("-----Upper---- ")
    # pprint(upper)
    # print("-----Lower---- ")
    # pprint(lower)



