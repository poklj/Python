import MongoDB.Mongo as mong
from pprint import pprint
#[35%] What were they watching?
# Print the titles of movies that have been rated by a given user.
# Accept (numeric) user_id interactively, quit when none is given.


def introLine():\
	"""
	Return back an Intro line
	:return: Pure printout
	"""
	
    print("\t ***** Pymongo Movie Ratings ***** \n"
          "\t  Enter a User_id to display the movies they have rated\n"
          "\t  if finished press [ENTER] without typing anything\n")


def grabUID(uid):
    """
    Grab a users 'Table"
    :param uid: User
    :return: the Users 'Table'
    """
    uid = int(uid)
    info_list = []

    info = ratings.find(
        {'user_id': uid}
    )
    for i in info:
        info_list.append(i)


    return info_list
    #Debug
    # pprint(info)
    # pprint(info_list)


def find_Pairs(list):
    """
	Match pairs of Movie Id's from the list
    :param list: InfoList
    :return: the matching pair from a Peice from InfoList
    """
    pairs = []
    for i in list:
        mid = i.get('movie_id')
        pairs.append(movies.find_one(
            {'_id': int(mid)}
        ))

    return pairs
    #pprint(pairs)


if __name__ == '__main__':
    Data = mong.Data() #Connect
    db = Data.Database #Pull the Database

    # Setup Collections for Join
    movies = db.movies
    ratings = db.ratings

    introLine()
    while True:
        uid = input("UserID ")
        if uid == "":
            break
        else:
            try:
                list = grabUID(uid)
                pairs = find_Pairs(list)
                for i in pairs:
                    print(i.get('title'))
            except ValueError:
                print("Please Enter Integers only")
                pass
