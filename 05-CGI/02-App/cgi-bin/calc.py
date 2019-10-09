import cgi

form = cgi.FieldStorage()

f_num = int(form.getvalue('f_num'))
s_num = int(form.getvalue('s_num'))

result = f_num + s_num

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1>Result is {}</h1>

</body>
</html>
""".format(result))