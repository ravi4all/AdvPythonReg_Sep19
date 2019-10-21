import cgi
import model

form = cgi.FieldStorage()
keys = form.keys()
ans = []
keys = sorted(keys)
for i in range(len(keys)):
    ans.append(form.getvalue(keys[i]))

count,correct_ans = model.checkAns(ans)

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
  <div class='container'>
    <h2>Questions</h2>
    <ul class='list-group'>
  """)
wrong_count = 0
for i in range(len(ans)):
    if ans[i] == correct_ans[i][0]:
        col = 'green'
    else:
        col = 'red'
        wrong_count += 1
    print("""
        <li class='list-group-item'>
            <h5 style='color:{};'>Ques {} => Your ans : {} | Correct ans : {}</h5>
        </li>
    """.format(col,i+1,ans[i],correct_ans[i][0]))
print("</ul>")
print("<br>")
print("<h4 class='text-center'>Final Result :</h4>")
print("<h5 class='text-center'>Correct Ans : {}".format(count))
print("<h5 class='text-center'>Wrong Ans : {}".format(wrong_count))
print("<h5 class='text-center'>Total : {}".format(count + wrong_count))
print("""
</body>
</html>
""")