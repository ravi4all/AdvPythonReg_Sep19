import cgi
import model

quesData = model.getQuestions()

questions = {
  "ques":{
    x : quesData[x] for x in range(len(quesData))
  }
}

form = cgi.FieldStorage()

if not form.getvalue('q_id'):
  q_id = 0
else:
  q_id = int(form.getvalue('q_id'))
  q_id += 1

current_ques = questions['ques'][q_id]

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
    <style>
        .card {
            border: none;
        }
        .product {
            border: 1px solid #eee;
            margin: 10px;
        }
    </style>
  </head>
  <body>
  <div class='container'>
    <h2>Questions</h2>
    <hr>
""")

print("""
<form action='testView.py' method='post'>
<h5>{}</h5>
<input type='hidden' value={} name='q_id'>
""".format(current_ques[0], q_id))
print("<ul class='list-groupd'>")
for i in range(1,5):
  print("""<li class='list-group-item'>
    <input type='radio' name='ans' value={}> {}</li>
  """.format(current_ques[i],current_ques[i]))
print("</ul>")

if q_id == len(quesData) - 1:
  submit_btn_state = ''
  next_btn_state = 'disabled'
else:
  submit_btn_state = 'disabled'
  next_btn_state = ''
print("<button class='btn btn-primary' {}>Next Question</button>".format(next_btn_state))
print("<button class='btn btn-primary disable-btn' {}>Submit</button>".format(submit_btn_state))
print("""
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
""")