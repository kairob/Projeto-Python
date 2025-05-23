from fakepinterest import database ,app


with app.app_context():
    database.create_all()
    print("Banco de dados criado com sucesso!")

