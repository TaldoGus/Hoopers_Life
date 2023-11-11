from flask import Flask, render_template, request, url_for, jsonify
app = Flask("name")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quem')
def quem():
    return render_template('quem.html')


@app.route('/dicas')
def dicas():
    return render_template('dicas.html')


@app.route('/onde')
def onde():
    return render_template('onde.html')

