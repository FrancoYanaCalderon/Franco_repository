from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///products.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price}, stock={self.stock})>"
#para inicializar la base de datos
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada satisfactoriamente")

#insertar productos
def insert_products():
    with app.app_context():
        p1 = Product(name="Cuaderno universitario", price=15.50, stock=100)
        p2 = Product(name="Bolígrafo azul", price=2.00,  stock=500)
        p3 = Product(name="Resaltador amarillo", price=5.75,  stock=200)
        p4 = Product(name="Regla 30 cm", price=3.00,  stock=150)
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.commit()
        print("Productos insertados")
#consultar productos
def query_products():
    with app.app_context():
        # Todos los registros
        print("\nListado de productos:")
        products = Product.query.all()
        for item in products:
            print(item)

        # Filtrados (stock mayor a 100)
        print("\nProductos con stock mayor a 100:")
        filtrados = Product.query.filter(Product.stock > 100).all()
        for item in filtrados:
            print(item)

        # Un solo registro
        print("\nObtener un solo producto (id=1):")
        product = Product.query.filter_by(id=1).first()
        if product:
            print(product)
        else:
            print("Producto no encontrado")

#actualizar un producto
def update_product():
    with app.app_context():
        print("\nActualización de un producto (id=4):")
        product = Product.query.filter_by(id=4).first()
        if product:
            product.name  = "Regla metálica 30 cm"
            product.price = 8.50
            product.stock = 80
            db.session.commit()
            print("Producto actualizado:", product)
        else:
            print("Producto no encontrado")
            
#eliminar un producto
def delete_product():
    with app.app_context():
        print("\nEliminación de un producto (id=3):")
        product = Product.query.filter_by(id=3).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            print("Producto eliminado satisfactoriamente")
        else:
            print("Producto no encontrado")
            
if __name__ == "__main__":
    init_db()
    insert_products()
    query_products()
    update_product()
    delete_product()