from database import db


class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    # Relacion con consultas
    consultas = db.relationship('Consulta', back_populates='paciente')

    def __init__(self, nombre, edad, direccion, telefono):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Paciente.query.all()

    @staticmethod
    def get_by_id(id):
        return Paciente.query.get(id)

    def update(self, nombre=None, edad=None, direccion=None, telefono=None):
        if nombre is not None:
            self.nombre = nombre
        if edad is not None:
            self.edad = edad
        if direccion is not None:
            self.direccion = direccion
        if telefono is not None:
            self.telefono = telefono
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
