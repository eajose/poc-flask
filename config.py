import os

SECRET_KEY = 'poc-flask'

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']

user = 'admin'
password = 'admin'
host = 'localhost'
database = 'poc-flask'
port = '5432'

DATABASE_CONNECTION_URI = f'posgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
SQLALCHEMY_DATABASE_URI = DATABASE_CONNECTION_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
