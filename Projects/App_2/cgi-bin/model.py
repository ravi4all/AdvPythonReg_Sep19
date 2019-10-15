import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='onlineshopping',autocommit=True)

cursor = connection.cursor()

class Product():

    def __init__(self,p_id,p_name,p_img,p_price):
        self.p_id = p_id
        self.p_name = p_name
        self.p_img = p_img
        self.p_price = p_price

def addToCart(p_id,p_name,p_img,p_price):
    prod = Product(p_id,p_name,p_img,p_price)
    query = "insert into cart_table values(%s,%s,%s,%s)"
    cursor.execute(query, (prod.p_id,prod.p_name,prod.p_img,prod.p_price))

