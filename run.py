from myapp.create_app import create_app
import os

app = create_app(os.getenv('ENV'))

if __name__ == '__main__':
    app.run()