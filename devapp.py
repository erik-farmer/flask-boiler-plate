from myapp import create_app

app = create_app.create_app({
    'erikMode': 'DEVELOPMENT',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
})

@app.errorhandler(500)
def handle_internal_server_error(e):
    return 'YOU GOOFED', 500