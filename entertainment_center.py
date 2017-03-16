import media #want to use contents of media.py 
import fresh_tomatoes #want to use contents of fresh_tomatoes.py

toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that come to life",
	"https://s-media-cache-ak0.pinimg.com/originals/1f/07/56/1f0756b0216f184ca6d2034b7c80b743.jpg",
	"https://youtu.be/KYz2wyBy3kc") #filename.classname 

gladiator = media.Movie("Gladiator", 
	"A general who became a slave, a slave who became a gladiator, a gladiator who defied meaning.",
	"https://www.movieposter.com/posters/archive/main/22/A70-11370",
	"https://youtu.be/owK1qxDselE") #filename.classname 

school_of_rock = media.Movie ("School of Rock", "A movie about a dude teaching a class to rock", 
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ18S_GJFZ3uVJJQVwtRrtQvk5LEhjCTkkJO-79a3j4zIKUnxw8lQ", 
	"https://youtu.be/XCwy6lW5Ixc")

midnight_in_paris = media.Movie ("Mightnight in Paris", "A movie about a hopeless romantic",
	"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
	"https://youtu.be/FAfR8omt-CY")

hunger_games = media.Movie ("Hunger Games", "A movie about crazy fucked up dystopian societies",
	"https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg",
	"https://youtu.be/EAzGXqJSDJ8")


print "Class Name:", media.Movie.__name__,"Docs:", media.Movie.__doc__, "Module Name:", media.Movie.__module__ 



#print media.Movie.valid_ratings #Print valid ratings Class variable.
movies = [toy_story, gladiator, school_of_rock, midnight_in_paris, hunger_games] #Create array of movies to be read by open_movies
fresh_tomatoes.open_movies_page(movies) # Takes in a list
#def run_trailer(movie_name):
#	str(movie_name).show_trailer()
#gladiator.show_trailer()

#print toy_story.storyline






