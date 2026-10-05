import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yq>z[0`L1l69Mc;{"Em8o+7W=Q5JQ|Q,S'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')