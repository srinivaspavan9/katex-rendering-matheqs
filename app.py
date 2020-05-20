from flask import Flask,render_template
import urllib.request,json
app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    file=open("templates/index.html",'w')
    s='''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous">
    <title>Sympy-Beta</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    </head>
    <body>
    <nav class="navbar navbar-light" style="background-color: #006400;">
        <a class="navbar-brand" style="color:azure;margin:auto;">SymPy-Beta</a>
    </nav>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.js" integrity="sha384-y23I5Q6l+B6vatafAwxRu/0oK/79VlbSz7Q9aiSZUvyWYIYsd+qj+o24G5ZU2zJz" crossorigin="anonymous"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/contrib/mathtex-script-type.min.js" integrity="sha384-LJ2FmexL77rmGm6SIpxq7y+XA6bkLzGZEgCywzKOZG/ws4va9fUVu2neMjvc3zdv" crossorigin="anonymous"></script>'''
    url="http://ravigitte.pythonanywhere.com/solve/?exp=integrate(2*x%20+%20y,x)"
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())
    for i in range(len(data)):
        if(i!=3):
            s=s+data[i]['output']
    s=s+'''<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>'''
    file.write(s)
    file.close()
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)