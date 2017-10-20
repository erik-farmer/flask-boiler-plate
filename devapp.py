from myapp import create_app

app = create_app.create_app({
    'env': 'DEVELOPMENT',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
})

if __name__ == '__main__':
    app.run(debug=True)