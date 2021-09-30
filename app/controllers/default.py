from flask import render_template
from app import app


@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template("index.html",
                            user=user) #busca o arquivo dento da pasta templates passando a varáavel user


@app.route("/test", defaults={'name': None}) #define o valor default do name para none
@app.route("/test/<name>") #passa um valor por padrão string pela url
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, Usuário!"


@app.route("/id/<int:id>")  # passa um valor inteiro pela url
def id(id):
    return "Seu Id é: %s!" % id

@app.route("/parouimpar/<int:number>", methods=['GET']) #limita o metodo http a ser usado nessa rota
def parouimpar(number):
    restoDiv = number % 2
    if restoDiv == 1:
        return "Impar"
    else:
        return "Par"
