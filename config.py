"""Configuración

Archivo de configuración de ambientes.
"""
from pathlib import Path
from dotenv import load_dotenv


def set_environtment_config():
    envfile = Path(__file__).parent.joinpath('config.env')
    if envfile.exists():
        load_dotenv(envfile)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = r"sqlite:///../config.db"

class ProductionConfig(Config):
    pass


if __name__ == '__main__':
    set_environtment_config()