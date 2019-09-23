from model import playList

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

def deleteSong(name):
    for i in range(len(playlist)):
        if playlist[i].name == name:
            del playlist[i]
            break
    return playlist

def searchSong(name):
    for i in range(len(playlist)):
        if playlist[i].name == name:
            return playlist[i]

def savePlaylist():
    playList.save(playlist)

def loadList():
    playList.load()