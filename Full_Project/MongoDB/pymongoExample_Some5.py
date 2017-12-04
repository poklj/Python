
__author__ = 'piotr'

from pymongo import MongoClient

# Authorized access required! (replace 'localhost' with IP of my mongoDB server)
cli=MongoClient('mongodb://student:mongoose@localhost/movieDB')


db = cli.movieDB

movies = db.movies
rating = db.ratings

score = 5
cnt = 15

# Not too bright an idea: looking at movies that scored 5 from *some* users
# There are quite many of those that I print the first cnt=15 only ;(

## card = rating.find({'rating' : score }).distinct('movie_id')
    # I commented out the above line (the 'old' way, doesn't work in mongo shell anymore)
    # and replaced it with this, which works in mongo shell too:
card = rating.distinct('movie_id', {'rating' : score })

print ('\n\t\t', cnt, 'Top-rated movies (out of ', len(card), ')\n' )

for val in card:
	if cnt :
		for film in movies.find({'_id' : val} ) :
			print ('\t' + film['title'])
			cnt = cnt - 1
	else :
		break

print ('\n\n')
