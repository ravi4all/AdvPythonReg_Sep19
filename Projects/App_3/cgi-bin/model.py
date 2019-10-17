import pymysql

connection = pymysql.connect(host="localhost",port=3306,
                             user="root",database="new_test",
                             autocommit=True)

cursor = connection.cursor()

class User():

    def __init__(self,id,name,pwd,course,sem,category):
        self.id = id
        self.name = name
        self.pwd = pwd
        self.course = course
        self.sem = sem
        self.category = category

def register(id,name,pwd,course,sem,category):
    obj = User(id,name,pwd,course,sem,category)
    query = "insert into users values (%s,%s,%s,%s,%s,%s,)"
    cursor.execute(query,(obj.name,obj.id,obj.pwd,obj.course,obj.sem,obj.category))

def login():
    pass

def getQuestions():
    query = "select * from questions"
    cursor.execute(query)
    data = cursor.fetchall()
    return data