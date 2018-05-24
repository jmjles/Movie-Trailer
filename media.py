import webbrowser


class Movie():
    """
        Recieves movie's info from
        entertainment_center.py
    """

    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        """ Taking input to sort out in a template. """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
