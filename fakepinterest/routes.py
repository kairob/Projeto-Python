from flask import render_template
from fakepinterest import app

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/contato')
def contato():
    return render_template('contato.html')    
@app.route('/usuario/<user>')
def usuario(user):
    return render_template('usuario.html', user=user)