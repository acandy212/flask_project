#app.py
#request is the data in out html
from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', methods=['POST'])
def addTodo():
    #access body information
    text1 = request.form['text1']
    print(text1)
    return(text1)


if __name__ == "__main__":
    app.run(debug=True)


#With GET, PUT, POST, DELETE you can pass information through the query and path parameters
#POST AND PUT the information will be passed within the body