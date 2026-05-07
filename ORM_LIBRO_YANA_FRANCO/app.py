from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configuración de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ─────────────────────────────────────────────
# Tabla intermedia N-M (Libro <-> Genero)
# ─────────────────────────────────────────────
libro_genero = db.Table(
    "libro_genero",
    db.Column("libro_id",  db.Integer, db.ForeignKey("libros.id"),  primary_key=True),
    db.Column("genero_id", db.Integer, db.ForeignKey("generos.id"), primary_key=True)
)

# ─────────────────────────────────────────────
# Definición de modelos
# ─────────────────────────────────────────────

class Autor(db.Model):
    __tablename__ = "autores"
    id           = db.Column(db.Integer, primary_key=True)
    nombre       = db.Column(db.String(100), nullable=False)
    nacionalidad = db.Column(db.String(60),  nullable=False)

    # Relación 1-N: un autor tiene muchos libros
    # cascade="all, delete-orphan" → al eliminar el autor, se eliminan sus libros
    libros = db.relationship("Libro", back_populates="autor", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Autor: nombre={self.nombre}, nacionalidad={self.nacionalidad}>"


class Genero(db.Model):
    __tablename__ = "generos"
    id     = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)

    # Relación N-M con Libro
    libros = db.relationship("Libro", secondary=libro_genero, back_populates="generos")

    def __repr__(self):
        return f"<Genero: nombre={self.nombre}>"


class Libro(db.Model):
    __tablename__ = "libros"
    id     = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    anio   = db.Column(db.Integer,     nullable=False)

    # Llave foránea → relación 1-N con Autor
    autor_id = db.Column(db.Integer, db.ForeignKey("autores.id"), nullable=False)

    # Relación inversa hacia Autor
    autor = db.relationship("Autor", back_populates="libros")

    # Relación N-M con Genero
    generos = db.relationship("Genero", secondary=libro_genero, back_populates="libros")

    def __repr__(self):
        return f"<Libro: titulo={self.titulo}, anio={self.anio}>"


# ─────────────────────────────────────────────
# Inicializar la base de datos
# ─────────────────────────────────────────────
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada satisfactoriamente")


# Insertar registros
def insert_data():
    with app.app_context():
        # Crear géneros
        g1 = Genero(nombre="Ficcion")
        g2 = Genero(nombre="Ciencia")
        g3 = Genero(nombre="Historia")
        g4 = Genero(nombre="Tecnologia")

        # Crear autores
        a1 = Autor(nombre="Gabriel Garcia Marquez", nacionalidad="Colombiana")
        a2 = Autor(nombre="Yuval Noah Harari",       nacionalidad="Israelita")
        a3 = Autor(nombre="Stephen Hawking",          nacionalidad="Britanica")

        # Crear libros y asociar autor + géneros
        l1 = Libro(titulo="Cien Anos de Soledad",         anio=1967, autor=a1)
        l2 = Libro(titulo="El amor en tiempos del colera", anio=1985, autor=a1)
        l3 = Libro(titulo="Sapiens: De animales a dioses", anio=2011, autor=a2)
        l4 = Libro(titulo="Homo Deus",                     anio=2015, autor=a2)
        l5 = Libro(titulo="Una Breve Historia del Tiempo", anio=1988, autor=a3)

        # Asociar géneros a libros (relación N-M)
        l1.generos.extend([g1, g3])       # Ficcion, Historia
        l2.generos.append(g1)             # Ficcion
        l3.generos.extend([g2, g3])       # Ciencia, Historia
        l4.generos.extend([g1, g2, g3])   # Ficcion, Ciencia, Historia
        l5.generos.extend([g2, g4])       # Ciencia, Tecnologia

        db.session.add_all([g1, g2, g3, g4, a1, a2, a3, l1, l2, l3, l4, l5])
        db.session.commit()
        print("Autores, libros y generos insertados correctamente")


# Consultar registros
def query_data():
    with app.app_context():
        print("\nListado de autores y sus libros")
        autores = Autor.query.all()
        for a in autores:
            print(f"\n{a.nombre} ({a.nacionalidad}) esta inscrito en:")
            for l in a.libros:
                print(f"\n - {l.titulo} ({l.anio})")

        print("\nListado de generos y sus libros")
        generos = Genero.query.all()
        for g in generos:
            print(f"\n{g.nombre} tiene inscritos a:")
            for l in g.libros:
                print(f"\n - {l.titulo} - {l.autor.nombre}")


# Actualizar registros
def update_data():
    with app.app_context():
        print("\nActualizando el titulo de un libro")
        libro = Libro.query.filter_by(id=3).first()

        if libro:
            libro.titulo = "Sapiens: A Brief History of Humankind"
            db.session.commit()
            print("Titulo actualizado correctamente")


# Eliminar registros (con cascada)
def delete_data():
    with app.app_context():
        print("\nEliminacion de un autor en cascada")
        autor = Autor.query.filter_by(id=3).first()

        if autor:
            db.session.delete(autor)
            db.session.commit()
            print("Autor eliminado junto con sus libros")
        else:
            print("Autor no encontrado")


if __name__ == "__main__":
    init_db()
    insert_data()
    query_data()
    update_data()
    delete_data()
    query_data()