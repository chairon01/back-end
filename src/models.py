from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(15), unique=True, nullable=False)

    def __init__(self, name,email,telefono):
        self.name = name
        self.email = email 
        self.telefono = telefono 

    def __repr__(self):
        return f'<User name: {self.name} email: {self.email} telefono: {self.telefono}>'

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "telefono": self.telefono
        }

class Presupuesto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servicios = db.Column(db.String(120), nullable = False)
    personas = db.Column(db.Integer, nullable = False ) 
    fecha = db.column(db.Date, nullable = False)

    def __init__(self, servicios, personas, fecha)
        self.servicios = servicios
        self.personas = personas
        self.fecha = fecha 

    def __repr__(self):
        return f'<Presupuesto servicios: {self.servicios} personas: {self.personas} fecha: {self.fecha}>'


    def serialize(self):
        return {
            "servicios": self.servicios,
            "personas": self.personas,
            "fecha": self.fecha
        }

    