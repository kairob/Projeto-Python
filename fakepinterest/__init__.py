from flask import Flask
from flask_sqlalchemy import SQLAlchemy         
from flask_login import LoginManager
from flask_bcrypt import Bcrypt                         

app = Flask(__name__)
#banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

app.config['SECRET_KEY'] = '6e75bc443279250d0a9e12a8e24e58d9'  # Substitua pela sua chave secreta
database = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'


#end banco de dados





from fakepinterest import routes
