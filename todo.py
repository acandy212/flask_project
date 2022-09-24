#app.py

from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', method={'POST'})
def addTodo():
    #access body information


if __name__ == "__main__":
    app.run(debug=True)


#With GET, PUT, POST, DELETE you can pass information through the query and path parameters
#POST AND PUT the information will be passed within the body