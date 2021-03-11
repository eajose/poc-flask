
from flask import Flask, render_template
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


# @app.route('/login')
# def login():
#     return render_template('login.html')


@app.route('/index')
def index():
    redis.incr('hits')
    return render_template('dashboard.html')
    # return (
    #     'This repository was created to practice development of microservices with Flask and this page has been viewed'
    #     ' %s time(s).' % redis.get('hits')
    #     )


@app.route('/tables')
def tables():
    return render_template('tables.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
