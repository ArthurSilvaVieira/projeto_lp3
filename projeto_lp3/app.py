# importa a class Flask do módulo flask
from flask import Flask, render_template
from validate_docbr import CPF, CNPJ
cpf = CPF()
cnpj = CNPJ()

# Instancia um objeto flask que representa a
# aplicação
app = Flask("Minha Aplicação")

# rota + função
# rota: definição de um padrão de url
# função: função python com retorno (string, template, outro)

# página home - /
@app.route("/")
def home():
    return render_template("home.html")

# página contato - /contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

# página produtos - /produtos
@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome": "Coca-cola", "descricao":"Mata a sede"},
        {"nome": "Doritos", "descricao":"Suja a mão"},
        {"nome": "Chocolote", "descricao":"Bom"},
    ]
    return render_template("produtos.html", produtos = lista_produtos)

#   página /servicos retornar "Nossos Servicos"
@app.route("/servicos")
def nossos_servicos():
    return "<h1>Nossos Servicos<h1>"

#   página /gerar-cpf retornar CPF aleatório
@app.route("/gerar-cpf")
def gerar_cpf():
    return f"CPF: {cpf.generate(True)}"

#   página /gerar-cpf retornar CPF aleatório
@app.route("/gerar-cnpj")
def gerar_cnpj():
    return f"CPF: {cnpj.generate(True)}"

app.run()