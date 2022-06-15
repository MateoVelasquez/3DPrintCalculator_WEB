"""Run
Script para ejecutar el aplicativo
"""
from flask_migrate import Migrate

from app import create_app, db


app = create_app()
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='localhost', port=7001)