#creating the Movie-Class as a blueprint for all movie-instances
class Movie():
    """This class provides a way to store movies"""
    def __init__(self, movie_title, movie_release,  movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.movie_release = movie_release
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
