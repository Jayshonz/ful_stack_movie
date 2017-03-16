import webbrowser


class Movie(): 
	""" This Class provides a way to store and organize movie related information """ 
	valid_ratings = ["G", "PG", "PG-13", "R"] #Class variable - these can be sharing by any class instance created. 

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): #every class - you need to define what init is - to initialize that instance of the class.
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self): #Instance Method - - a function within a class ClassName(object):
		webbrowser.open(self.trailer_youtube_url)
			