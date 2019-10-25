import cgi
import model

form = cgi.FieldStorage()

id = form.getvalue('user_id')
pwd = form.getvalue('user_pwd')

user = model.login(id,pwd)

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

def showProfile():
    print("""
    <div class='container'>
        <div class='row'>
            <div class='col-md-4'>
                <img class='w-100' src='../user_profilePic/{}'>
            </div>
            <div class='col-md-8'>
                <h5>Name : {}</h5>
                <h5>ID : {}</h5>
                <h5>Course : {}</h5>
                <h5>Semester : {}</h5>
                <a href='testView.py' class='btn btn-primary'>Start Test</a>    
            </div>
        </div>
    </div>
    """.format(user[0][-1], user[0][0], user[0][1],user[0][3],user[0][4]))

if isinstance(user,str):
    print("<h2>Login Failed...</h2>")
    print("<a href='../index.html'>Try Again</a>")
else:
    showProfile()

print("""
</body>
</html>
""")
