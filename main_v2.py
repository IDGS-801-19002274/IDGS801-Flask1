from flask import Flask

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

if __name__ == "__main__":
    app.run(debug = True, port=3000)