from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/a')
def a():
    return render_template('otro.html')

if __name__ == "__main__":
    app.run(debug = True, port=3000)