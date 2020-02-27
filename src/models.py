from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    """Tabla-De-User"""

    email = db.Column(db.String(40), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    def __init__(self, email, name):
        
        self.name= name
        self.email= email

    def __repr__(self):
        return f'<User  email: {self.email} name: {self.name}>'

    def serialize(self):
        return {
            "email": self.email,
            "name": self.name
        }

class Presupuesto(db.Model):
    """Tabla-De-Presupuesto"""
    
    id = db.Column(db.Integer, primary_key=True)
    evento = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), nullable=False)
    personas = db.Column(db.Integer, nullable = False )
    direccion = db.Column(db.String(250), nullable = False)
    fecha = db.Column(db.Date, unique=True, nullable = False)
    hora = db.Column(db.Time, nullable=False)
    telefono = db.Column(db.String(50), nullable = False)    

    def __init__(self, evento, email, personas, direccion, fecha, hora , telefono):
        self.evento = evento
        self.email = email
        self.personas = personas
        self.direccion = direccion
        self.fecha = fecha 
        self.hora = hora
        self.telefono = telefono

    def __repr__(self):
        return f'<Presupuesto evento: {self.evento} email: {self.email} personas: {self.personas} direccion: {self.direccion} fecha: {self.fecha} hora: {self.hora} telefono: {self.telefono}>'


    def serialize(self):
        return {
            "evento": self.evento,
            "email": self.email,
            "personas": self.personas,
            "direccion": self.direccion,
            "fecha": self.fecha,
            "hora": self.hora,
            "telefono": self.telefono
        }

    