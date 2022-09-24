#app.py
#request is the data in out html
from flask import Flask, render_template, request
app = Flask(__name__)

todoList = []

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', methods=['POST'])
def addTodo():
    #access body information
    todoItem = request.form['text1']
    todoList.append(todoItem)
    return render_template('home.html', todoList=todoList)


if __name__ == "__main__":
    app.run(debug=True)


#With GET, PUT, POST, DELETE you can pass information through the query and path parameters
#POST AND PUT the information will be passed within the body