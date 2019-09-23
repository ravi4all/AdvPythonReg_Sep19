import sys
sys.path.append('..')

from model import model

def addSong(name,singer,movie):
    playList = model.addSong(name,singer,movie)
    return playList

def deleteSong(name):
    playList = model.deleteSong(name)
    return playList

def searchSong(name):
    songObj = model.searchSong(name)
    return songObj

def savePlaylist():
    model.savePlaylist()