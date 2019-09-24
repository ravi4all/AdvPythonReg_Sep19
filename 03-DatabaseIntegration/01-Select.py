import pymysql

connection = pymysql.connect(host="localhost",port=3306,user="root",database="music_player",
                             autocommit=True)

cursor = connection.cursor()

query = "select * from playlist"
cursor.execute(query)

data = cursor.fetchall()
print(data)