class Song:
    song_count = 0
    genre_count = {}
    artist_count = {}
    genres = []
    artist = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()  
        Song.add_to_genres(genre)
        Song.add_to_artist(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.song_count += increment
    
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)
    
    @classmethod
    def add_to_artist(cls, artist):
        cls.artist.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

#example
song1 = Song("song1", "artist1", "genre1")
song2 = Song("song2", "artist2", "genre2")
song3 = Song("song3", "artist3", "genre3")
song4 = Song("song4", "artist4", "genre4")
song5 = Song("song5", "artist5", "genre5")
print(Song.song_count)
print(Song.genres)
print(Song.artist)
print(Song.genre_count)
print(Song.artist_count)

