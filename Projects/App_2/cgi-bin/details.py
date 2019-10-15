import pymysql
import base
import cgi

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='onlineshopping',autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()
p_id = form.getvalue('id')
query = "select * from productdetails where p_id = %s"
cursor.execute(query,p_id)
p_details = cursor.fetchall()

query = "select * from products where p_id = %s"
cursor.execute(query,p_id)
product = cursor.fetchall()

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
  <body>""")

base.header()
discount = product[0][2] + 5500
print("""
<div class='container'>
    <h2 class='text-center'>Product Details</h2>
    <hr>
    <div class='row'>
        <div class='col-md-5'>
            <img src={} class='w-100'>
        </div>
        <div class='col-md-7'>
            <h4>Product : {} </h4>
            <h5>Price : {} Rs <del>{}</del> </h5>
            <p>Rating : {}</p>
            <p>Offers : {}</p>
            <h5>Highlights</h5>
            <p>{}</p>
            <p><b>Description</b> : {}</p>
            <form action='cartController.py'>
    <input type='hidden' name='p_id' value={}>
        <button type='submit' class='btn btn-primary'>Add to Cart </button>
    </form>
        </div>
    </div>
</div>
""".format(product[0][3],
           product[0][1],
           product[0][2],
           discount,
           p_details[0][2],
           p_details[0][3],
           p_details[0][4],
           p_details[0][1],
           product[0][0]
           ))

print("""
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
""")