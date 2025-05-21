from fakepinterest import database  
from datetime import datetime

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(200), nullable=False)
    profile_picture = database.relationship('ProfilePicture', backref='user',lazy=True, uselist=False)

    

class ProfilePicture(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String(200), default='default.png')
    data_upload = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)