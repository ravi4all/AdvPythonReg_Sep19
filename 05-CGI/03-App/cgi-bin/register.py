import cgi
import pymysql

form = cgi.FieldStorage()

name = form.getvalue('reg_name')
email = form.getvalue('reg_email')
pwd = form.getvalue('reg_pwd')

