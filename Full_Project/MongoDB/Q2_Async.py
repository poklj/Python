import MongoDB.Mongo as mong
from pprint import pprint
import asyncio

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

def count(Llist):
    """
    Count the amount of users in a list
    :param Llist: List of users
    :return:
    """
    count = 0
    for i in Llist:
        count += 1

    return count

async def GrabRatings(List):
    """
    Grab the ratings of every User
    :param List: User List
    :return: List of ratings
    """
    ratingL = []
    for i in List:
        a = ratings.find({
            'user_id': i.get('_id')
        })
        print(a)
        for i in a:
            ratingL.append(i.get('rating'))
            print(i)

    return ratingL

def avg(rating, count):
    """
    Calculate the Average Rating of the list
    :param List: Userlist
    :return: The average
    """
    count = count(list)
    ratings = GrabRatings(list)

    fullrating = 0
    for i in count:
        ratings += i

    return (fullrating/count)



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

    countUpper = count(upper)
    countLower = count(lower)

    loop = asyncio.get_event_loop()
    tasks = {
        asyncio.ensure_future(GrabRatings(upper)),
        rLower = GrabRatings(lower)
    }

    aUpper = avg(count=countUpper, rating=rUpper)
    aLower = avg(count=countLower, rating=rLower)



    print(aUpper)
    print(aLower)
    #upperCount = count(upper)
    #lowerCount = count(lower)

    # print("-----Upper---- ")
    # pprint(upper)
    # print("-----Lower---- ")
    # pprint(lower)



