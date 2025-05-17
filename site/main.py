from flask  import Flask

app = Flask(__name__)
@app.route('/') 
def homepage ():
    return 'Hello, World!'
@app.route('/perfil')
def perfil():
    return 'This is the/perfil page.'    ,
@app.route('/contato')
def contato():
    return 'This is the contato page.'  

    
if __name__ == '__main__':
    app.run(debug=True)
