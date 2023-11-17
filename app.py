from flask import Flask, render_template, request, url_for, jsonify
app = Flask("name")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posicoes')
def posicoes():
    return render_template('posicoes.html')


@app.route('/dicas')
def dicas():
    return render_template('dicas.html')


@app.route('/nba')
def nba():
    return render_template('nba.html')

