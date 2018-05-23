from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

PORT = 8080
DEBUG = True
POSTGRES_CONFIG = {
    'user': 'username',
    'pw': 'password',
    'db': 'postgres',
    'host': '127.0.0.1',
    'port': '5432'}

app = Flask(__name__)
db = SQLAlchemy(app)

# MODEL DEFINITION
class Phrase(db.Model):
    __tablename__ = 'phrases'
    id = db.Column('id', db.Integer, primary_key=True)
    phrase = db.Column('phrase', db.String, nullable=False)

    def __init__(self, phrase):
        self.phrase = phrase

    def __repr__(self):
        return '<{}:{}>'.format(id, phrase)


# INITIALISE DATABASE
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(**POSTGRES_CONFIG)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.create_all()


@app.route('/write', methods=['POST'])
def write():
    post = request.get_json()
    phrase = post['phrase']
    db.session.add(Phrase(phrase))
    db.session.commit()
    return "Added to database: {}".format(phrase)


@app.route('/read')
def read():
    phrase_list = Phrase.query.with_entities(Phrase.phrase).all()
    phrase_list = [phrase[0] for phrase in phrase_list]
    return json.dumps({"phrases": phrase_list})


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)
