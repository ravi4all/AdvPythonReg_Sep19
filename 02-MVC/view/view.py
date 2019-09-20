# CRUD - Create Read Update Delete

import sys
sys.path.append("..")

from controller import controller

def add():
    name = input("Enter song name : ")
    singer = input("Enter singer name : ")
    movie = input("Enter movie name : ")
    playList = controller.addSong(name,singer,movie)
    print("Song added to playlist")
    for song in playList:
        s = str(song).split(",")
        print("Song Name :",s[0])
        print("Singer :",s[1])
        print("Movie :",s[2])
        print("---------------------")

def delete():
    pass

def search():
    pass

def main():
    print("""
    1. Add Song to Playlist
    2. Delete Song from Playlist
    3. Search Song
    """)

    ch = input("Enter your ch : ")
    opr = {
        "1" : add,
        "2" : delete,
        "3" : search
    }
    opr.get(ch)()

while True:
    main()