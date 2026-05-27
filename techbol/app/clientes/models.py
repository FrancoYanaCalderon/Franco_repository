from app import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String, nullable=False)

    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)

    def __repr__(self):
        return f"<CLIENTE: {self.nombre} - {self.telefono}>"
