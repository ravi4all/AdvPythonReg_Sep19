import pymysql
import os

connection = pymysql.connect(host="localhost",port=3306,
                             user="root",database="new_test",
                             autocommit=True)

cursor = connection.cursor()

class User():

    def __init__(self,id,name,pwd,course,sem,category,pic):
        self.id = id
        self.name = name
        self.pwd = pwd
        self.course = course
        self.sem = sem
        self.category = category
        self.pic = pic

def register(name,id,pwd,course,sem,category,pic):
    if pic.filename:
        fn = os.path.basename(pic.filename)
        img = pic.file.read()
        file = open("user_profilePic/"+fn, 'wb')
        file.write(img)
        file.close()
    else:
        fn = "defaultImg.gif"
    obj = User(id,name,pwd,course,sem,category,fn)
    query = "insert into users values (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(obj.name,obj.id,obj.pwd,obj.course,obj.sem,obj.category,obj.pic))

def login(id,pwd):
    query = "select * from users where id=%s and pwd = %s"
    cursor.execute(query, (id,pwd))

    if cursor.rowcount < 1:
        data = "Invalid User ID or Password"
    else:
        data = cursor.fetchall()

    return data

def getQuestions():
    query = "select * from questions"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def checkAns(ans):
    query = "select ans from questions"
    cursor.execute(query)
    data = cursor.fetchall()
    count = 0
    for i in range(len(ans)):
        if data[i][0] == ans[i]:
            count += 1
    # print(count)
    return count,data