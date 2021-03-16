from flask import Flask, config
from models.models import db
from redis import Redis



app = Flask(__name__)
redis = Redis(host='redis', port=6379)
app.config.from_pyfile('config.py')
# app.app_context().push()
# db.init_app(app)
# db.create_all()

from views import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
