from myapp import create_app

app = create_app.create_app({
    'erikMode': 'DEVELOPMENT',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
})