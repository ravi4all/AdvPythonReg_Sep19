import pymysql

connection = pymysql.connect(host="localhost",port=3306,user="root",database="music_player",
                             autocommit=True)

cursor = connection.cursor()

def insert(song,singer,movie):

    query = "insert into playlist values (%s,%s,%s)"
    cursor.execute(query, (song, singer, movie))

def select():
    pass