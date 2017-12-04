import MongoDB.Mongo as mong
from pprint import pprint

# [35%] Are the older people more grumpy?
# Print the average scores given by users of age N or over, and those below N,  where N takes values, 30, 40, 45, 50.
# Any comments?

def grabUsers():
    """
	Grab the ENTIRE user list Database
    :return: List appeneded userlist
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
        elif (i.get('age') < nAge):
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

# def GrabRatings(List):
#     """
#     Grab the ratings of every User
#     :param List: User List
#     :return: List of ratings
#     """
#     ratingL = []
#     for i in List:
#         a = ratings.find({
#             'user_id': i.get('_id')
#         })
#         #print(a)
#         for i in a:
#             ratingL.append(i.get('rating'))
#             #print(i)
#
#     return ratingL

def GrabRatingsv2(List):
	"""
	use the Entire Ratings list to find the average of the user 
	:param List: the userlist
	:return: The Ratings list appened with the ratings of every user
	"""

    ratingL = []

    RatingsList = ratings.find({})
    for i in List:
        for x in RatingsList:
            #print(x)
            if i.get('_id') == x.get('user_id'):
                ratingL.append(x.get('rating'))
                #print(ratingL)

    return ratingL

def avg(rating, count=0):
	"""
	
	:param: Deprecated
	:param rating: The rating list
	:return: Average
	"""

    a = 0
    if len(rating):
        b = len(rating)
    else:
        b = 1

    for i in rating:
        a += i
    return (a/b)
# For i in each User Check Rating User ID
    # if True, append Rating


if __name__ == '__main__':
    Data = mong.Data()  # Connect
    db = Data.Database  # Pull the Database

    # Setup Collections for Join
    movies = db.movies
    ratings = db.ratings
    users = db.users

    while True:
        try:
            age = input("Input user Age to split by ")
            try:
                null = float(age)
            except:
                raise ValueError
            if age is str:
                raise ValueError
            if age is tuple:
                raise ValueError
            if age is list:
                raise ValueError
            print("Working...")
            break
        except ValueError:
            print("Please Input a Age")

    userL = grabUsers()
    # pprint(userL)
    splitCompile = userSplit(float(age), userL)

    upper = splitCompile[0]
    lower = splitCompile[1]

    countUpper = count(upper)
    countLower = count(lower)

    rUpper = GrabRatingsv2(upper)
    rLower = GrabRatingsv2(lower)

    aUpper = avg(count=countUpper, rating=rUpper)
    aLower = avg(count=countLower, rating=rLower)

    print('The average rating of people aged {0} and above is: {1}'.format(age, aUpper))
    print('The average rating of people aged {0} and below is: {1}'.format(age, aLower))
    #upperCount = count(upper)
    #lowerCount = count(lower)

    # print("-----Upper---- ")
    # pprint(upper)
    # print("-----Lower---- ")
    # pprint(lower)



