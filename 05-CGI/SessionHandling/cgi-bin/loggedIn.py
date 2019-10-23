import cgi, random
from http import cookies
import UserInfo
import os

form = cgi.FieldStorage()

def showLoginScreeen(email,cook):
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>

    <h1>Welcome {}</h1>

    <p>Session created and values are : {}</p>

    <a href='profile.py'>Visit Your Profile</a>
    <a href='logout.py'>Log out</a>

    </body>
    </html>
    """.format(email, cook.output()))

# def setSessionId(sessId):
#   pass

if not form.getvalue('email') and not form.getvalue('pwd'):
    pass
    # print("Content-type:text/html\r\n\r\n")
    # if "HTTP_COOKIE" in os.environ:
        # cook = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
        # sess_id = cook['sessionId'].value
else:
    email = form.getvalue('email')
    pwd = form.getvalue('pwd')
    cook = cookies.SimpleCookie()
    sessId = random.randint(1, 1000000000)
    cook['sessionId'] = sessId
    print(cook)
    UserInfo.UserSessionInfo.setSession((sessId,email))
    showLoginScreeen(email,cook)
