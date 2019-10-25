import cgi
import model

form = cgi.FieldStorage()

name = form.getvalue('user_name')
id = form.getvalue('user_id')
pwd = form.getvalue('user_pwd')
course = form.getvalue('course')
sem = form.getvalue('sem')
cat = form.getvalue('cat')
pic = form['profile']

model.register(name,id,pwd,course,sem,cat,pic)

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
  """)
print("<h2>Registered Successfully...</h2>")
print("<a href='../index.html'>Login Now</a>")
print("""
</body>
</html>
""")
