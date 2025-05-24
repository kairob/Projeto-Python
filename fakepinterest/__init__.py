from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade1.db'
database = SQLAlchemy(app)


#end banco de dados





from fakepinterest import routes
