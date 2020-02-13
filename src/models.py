from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    """Tabla-De-User"""
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(40), primary_key=True, unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    
    def __init__(self, name, email, telefono):
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
    """Tabla-De-Presupuesto"""
    
    id = db.Column(db.Integer, primary_key=True)
    servicios = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), nullable=False)
    personas = db.Column(db.Integer, nullable = False )
    direccion = db.Column(db.String(250), nullable = False)
    fecha = db.Column(db.DateTime, unique=True, nullable = False)
    

    def __init__(self, servicios, email, personas, direccion, fecha):
        self.servicios = servicios
        self.email = email
        self.personas = personas
        self.direccion = direccion
        self.fecha = fecha 

    def __repr__(self):
        return f'<Presupuesto servicios: {self.servicios} email: {self.email} personas: {self.personas} direccion: {self.direccion} fecha: {self.fecha}>'


    def serialize(self):
        return {
            "servicios": self.servicios,
            "email": self.email,
            "personas": self.personas,
            "direccion": self.direccion,
            "fecha": self.fecha
        }

    