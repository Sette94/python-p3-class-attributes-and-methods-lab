# import ipdb


class Song:

    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    names = []

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genre(self)
        self.add_to_artists(self)
        self.add_to_names(self)
        self.add_to_genre_count(self)
        self.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genre(cls, self):
        if self.genre not in cls.genres:
            cls.genres.append(self.genre)
        else:
            print("Duplicate genre")

    @classmethod
    def add_to_artists(cls, self):
        if self.artist not in cls.artists:
            cls.artists.append(self.artist)
        else:
            print("Duplicate artist")

    @classmethod
    def add_to_names(cls, self):
        if self.name not in cls.names:
            cls.names.append(self.name)
        else:
            print("Duplicate song")

    @classmethod
    def add_to_genre_count(cls, self, increment=1):

        if self.genre in cls.genre_count:
            cls.genre_count[self.genre] += 1
        else:
            cls.genre_count[self.genre] = 1

    @classmethod
    def add_to_artist_count(cls, self, increment=1):

        if (cls.artist_count == {}):
            cls.artist_count.update(
                {
                    self.artist: 1
                }
            )
        else:
            for key in list(cls.artist_count.keys()):
                if (self.artist == key):
                    cls.artist_count[key] += increment

                else:
                    cls.artist_count[self.artist] = 1
                    pass


# ipdb.set_trace()
