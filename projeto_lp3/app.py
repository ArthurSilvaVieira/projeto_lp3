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
        {"nome": "Jacaré de Papo Amarelo", "descricao":"Pet médio, filhote", "imagem": "https://agorarn.com.br/files/uploads/2022/04/get-3-e1650037372308.jpg"},
        {"nome": "Jacaré Açu", "descricao":"Pet grande, filhote", "imagem": "https://c8.alamy.com/comp/MBYKBT/a-baby-caiman-caught-and-presented-by-a-keeper-in-the-amazon-rainforest-tambopata-national-reserve-puerto-maldonado-peru-MBYKBT.jpg"},
        {"nome": "Jacaretinga", "descricao":"Pet pequeno, filhote", "imagem": "https://www.mundoecologia.com.br/wp-content/uploads/2019/08/Filhote-de-Jacaretinga.jpg"},
    ]
    return render_template("produtos.html", produtos = lista_produtos)

#   página /servicos retornar "Nossos Servicos"
@app.route("/servicos")
def nossos_servicos():
    return "<h1>Nossos Servicos<h1>"

#   página /gerar-cpf retornar CPF aleatório
@app.route("/gerar-cpf")
def gerar_cpf():
    cpf_gerado = cpf.generate(True)
    return render_template("cpf.html", cpf_gerado = cpf_gerado)


#   página /gerar-cpf retornar CPF aleatório
@app.route("/gerar-cnpj")
def gerar_cnpj():
    cnpj_gerado = cnpj.generate(True)
    return render_template("cnpj.html", cnpj_gerado = cnpj_gerado)

#   página politicas de privacidade - /politicas-de-privacidade
@app.route("/politicas-de-privacidade")
def politica_privacidade():
    return render_template("politica-privacidade.html")

@app.route("/como-utilizar")
def como_utilizar():
    return render_template("como-utilizar")

@app.route("/termos-de-uso")
def termos_de_uso():
    return render_template("termos-de-uso.html")


app.run()