import cgi
import model

quesData = model.getQuestions()

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
    <ul class='list-group'>
  """)

for i in range(len(quesData)):
    print("""
        <li class='list-group-item'>
            <p>{}. {}</p>
            <p><input type='radio' value={}> {}</p>
            <p><input type='radio' value={}> {}</p>
            <p><input type='radio' value={}> {}</p>
            <p><input type='radio' value={}> {}</p>
        </li>            
    """.format(i+1,quesData[i][0],
               quesData[i][1],quesData[i][1],
               quesData[i][2], quesData[i][2],
               quesData[i][3], quesData[i][3],
               quesData[i][4], quesData[i][4]))

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