from fakepinterest import database  ,app
# from fakepinterest import database
from fakepinterest.models import User, ProfilePicture
with app.app_context():
    database.create_all()
    print("Banco de dados criado com sucesso!")