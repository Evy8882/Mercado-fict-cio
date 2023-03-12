from flask import Flask, render_template
from db import db

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/page/caderno-turquesa-tilibra')
def caderno_turquesa_tilibra():
    return render_template('page.html', dados = db['caderno'])

@app.route('/page/bolsa-de-couro-arzon')
def bolsa_de_couro_arzon():
    return render_template('page.html', dados = db['bolsa'])

@app.route('/page/cadeira-de-madeira-texas')
def cadeira_de_madeira_texas():
    return render_template('page.html', dados = db['cadeira'])

@app.route('/page/cadeira-gamer-xzone-verde')
def cadeira_gamer_xzone_verde():
    return render_template('page.html', dados = db['cadeira_gamer'])

@app.route('/page/ventilador-de-mesa-mondial')
def ventilador_de_mesa_mondial():
    return render_template('page.html', dados = db['ventilador'])

@app.route('/page/panela-tramontina-vermelha')
def panela_tramontina_vermelha():
    return render_template('page.html', dados = db['panela'])

@app.route('/page/escova-de-cabelo-ricca-oval-roxa')
def escova():
    return render_template('page.html', dados = db['escova'])

@app.route('/page/tenis-all-stars')
def tenis_all_stars():
    return render_template('page.html', dados = db['tenis'])

@app.route('/page/camisa-social-preta')
def camisa_social_preta():
    return render_template('page.html', dados = db['camisa'])

@app.route('/page/bola-de-futebol')
def bola_de_futebol():
    return render_template('page.html', dados = db['bola'])


if __name__ == '__main__':
    app.run(debug=True)