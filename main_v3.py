from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo Flask"

@app.route('/Hola')
def hola():
    return "Hola desde hola"

@app.route('/Nueva')
def nueva():
    return "Hola desde Nueva"

@app.route('/Menu')
def menu():
    return "<h1>Hola</h1>"

@app.route('/User/<string:user>')
def user(user):
    return "Hola " + user

@app.route('/Numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/User/<int:id>/<string:name>')
def idUser(id, name):
    return "ID: {}, Usuario: {}".format(id, name)

@app.route('/Suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return "La suma es: {}".format(num1 + num2)

@app.route('/Formulario', methods=["GET", 'POST'])
def formulario():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        return "<h2>La suma es: {}</h2>".format(str(int(num1) + int(num2)))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True, port=3000)