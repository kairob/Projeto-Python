from fakepinterest import database ,app
from fakepinterest.models import Usuario, Foto


with app.app_context():
    database.create_all()
    print("Banco de dados criado com sucesso!")

