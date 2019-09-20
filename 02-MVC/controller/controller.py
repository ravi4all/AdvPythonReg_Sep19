import sys
sys.path.append('..')

from model import model

def addSong(name,singer,movie):
    playList = model.addSong(name,singer,movie)
    return playList