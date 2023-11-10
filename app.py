from flask import Flask, render_template, request, url_for, jsonify
app = Flask("name")
@app.route('/')
def home():
    return render_template('index.html')