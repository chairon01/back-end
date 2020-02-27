"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, make_response
import json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, User, Presupuesto
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route('/register', methods=['POST'])
def register_user():
    user_data = request.json
    new_user = User(user_data["email"],user_data["name"])
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"result": "user registered"}), 201
    except:
        db.session.rollback()
        return jsonify({"result": "user already exists or input is not valid"}), 400

@app.route('/presupuesto', methods=['POST'])
def presupuesto_user():
    presupuesto_data = request.json
    print(presupuesto_data)
    if "personas" in presupuesto_data:
        print("got here")
        new_presupuesto = Presupuesto(presupuesto_data["evento"], presupuesto_data["email"],presupuesto_data["personas"],presupuesto_data["direccion"],presupuesto_data["fecha"],presupuesto_data["hora"],presupuesto_data["telefono"])
    else:
        new_presupuesto = Presupuesto(presupuesto_data["evento"], presupuesto_data["email"],presupuesto_data["direccion"],presupuesto_data["fecha"],presupuesto_data["hora"],presupuesto_data["telefono"])
    db.session.add(new_presupuesto)
    if presupuesto_data["suscribir"] == True:
        if User.query.filter_by(email=presupuesto_data["email"]).one_or_none():
            new_user = User(presupuesto_data["email"], presupuesto_data["name"])
            db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify("Su presupuesto se completo con éxito"), 200
    except:
        db.session.rollback()
        return jsonify({"result": "Debe completar su registro"}), 400
    

# this only runs if `$ python src/main.py` is executed
    if __name__ == '__main__':
        PORT = int(os.environ.get('PORT', 3000))
        app.run(host='0.0.0.0', port=PORT, debug=False)
