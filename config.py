SECRET_KEY = ' '

SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(

    SGBD = 'mysql+mysqlconnector',
    usuario = '',
    senha = '',
    servidor = 'localhost',
    database = 'jogoteca'
)

#colocar uma secret_key e o seu usuário e senha