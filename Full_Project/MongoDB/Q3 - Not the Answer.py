import MongoDB.Mongo as mong
# [40%] Do not watch these!
# Find the "worst movies" and print their titles.
# (First state, and then use your criteria on what constitutes "the worst")
# The worst movies are ones who's ratings have one person who dislikes the movie




if __name__ == '__main__':
    Data = mong.Data() #Connect
    db = Data.Database #Pull the Database

    # Setup Collections for Join
    movies = db.movies
    ratings = db.ratings

    allRatings = ratings.find({})

    for i in allRatings:
        if i.get('rating') <= 1:
            movies.find_one({
                '_id': i.get('movie_id')
            }).get('title'))