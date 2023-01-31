from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/calcular', methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route('/resultado', methods=['POST'])
def calcular():
    n1 = request.form.get("txtNum1")
    n2 = request.form.get("txtNum2")
    res = int(n1) * int(n2)
    return render_template("usuarios.html", res, n1, n2)

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

if __name__ == "__main__":
    app.run(debug = True, port=3000)