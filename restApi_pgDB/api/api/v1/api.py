from flask import Flask, request, jsonify
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
db = SQLAlchemy(app)
marsh = Marshmallow(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column('person_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'age')


person_schema = PersonSchema(strict=True)
persons_schema = PersonSchema(many=True, strict=True)


@app.route('/api/v1/persons', methods=['POST'])
def add_person():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, location='json')
    parser.add_argument('age', type=int, required=True, location='json')

    args = parser.parse_args(strict=True)

    new_person = Person(args['name'], args['age'])

    db.session.add(new_person)
    db.session.commit()

    return person_schema.jsonify(new_person)


@app.route('/api/v1/persons/age=<int:x>', methods=['GET'])
def get_persons_by_age(x):
    persons = Person.query.filter(Person.age==x).all()
    result = persons_schema.dump(persons)
    return jsonify(result.data)


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...\n'


if __name__ == '__main__':
    db.create_all()
    app.run()
