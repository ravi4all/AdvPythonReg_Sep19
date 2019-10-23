from http import cookies
import os
import UserInfo
import loggedIn

def showError():
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>

        <h1>Login First</h1>

        </body>
        </html>
        """)

def showProfile(sess):
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>

    <h1>Welcome {}</h1>

    <a href='profile.py'>Visit Your Profile</a>
    <a href='loggedIn.py'>Back to Home</a>
    <a href='logout.py'>Log out</a>

    </body>
    </html>
    """.format(sess))

print("Content-type:text/html\r\n\r\n")
if "HTTP_COOKIE" in os.environ:
    cook = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    if cook:
        sess_id = cook['sessionId'].value
        # email = UserInfo.UserSessionInfo.info[sess_id]
        showProfile(UserInfo.UserSessionInfo.getSession())
    else:
        showError()
else:
    print("HTTP_COOKIE not set!")