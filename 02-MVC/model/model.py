class Song():

    def __init__(self,name,singer,movie):
        self.name = name
        self.singer = singer
        self.movie = movie

    def __str__(self):
        return self.name + "," + self.singer + "," + self.movie

playlist = []
def addSong(name,singer,movie):
    song = Song(name,singer,movie)
    playlist.append(song)
    return playlist