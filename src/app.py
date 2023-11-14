import socket
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:admin123@127.0.0.1:3307/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking as it can be resource-intensive
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/')
def hello_world():
    return "Hello! I am a Flask application running on {}".format(socket.gethostname())


if __name__ == '__main__':
    # Note the extra host argument. If we didn't have it, our Flask app
    # would only respond to requests from inside our container
    app.run(host='0.0.0.0')
