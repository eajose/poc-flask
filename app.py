# compose_flask/app.py
from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    return (
        'This repository was created to practice development of microservices with Flask and this page has been viewed'
        ' %s time(s).' % redis.get('hits')
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
