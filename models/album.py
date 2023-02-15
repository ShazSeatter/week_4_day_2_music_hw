class Album:

    def __init__(self, title, genre, artist, id = None):
        self.title = title
        self.genre = genre
        self.artist = artist # referencing artist 
        self.id = id
