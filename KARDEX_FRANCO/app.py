from flask import Flask, request, render_template, url_for, redirect
import sqlite3
app = Flask(__name__)

# creacion de base de datos y tablas segun la estructura
def init_database():
    #creamos la base de datos o nos conectamos a la BD
    conn = sqlite3.connect("kardex.db")
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS personas(
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            fecha_nac DATE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

#inicializando la creacion de la BD   
init_database()

@app.route("/")
def index():
    #conexion a la BD
    conn = sqlite3.connect("kardex.db")
    #permite manejar registros en forma de diccionario
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas")
    personas = cursor.fetchall()
    return render_template('index.html', personas = personas)
@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/save", methods=['POST'])
def save():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    fecha_nac = request.form['fecha_nac']
    
    conn = sqlite3.connect("kardex.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO personas (nombre, telefono, fecha_nac)
        VALUES (?,?,?)
        """,
        (nombre, telefono, fecha_nac)
        )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/edit/<int:id>")
def persona_edit(id):
    #conexion a la BD
    conn = sqlite3.connect("kardex.db")
    #permite manejar registros en forma de diccionario
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas WHERE id = ?", (id,))
    persona = cursor.fetchone()
    conn.close()
    return render_template("edit.html", persona = persona)

@app.route("/update", methods = ['POST'])
def persona_update():
    id = request.form['id']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    fecha_nac = request.form['fecha_nac']
    
    conn = sqlite3.connect("kardex.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE personas SET nombre = ?, telefono = ?, fecha_nac = ? WHERE id = ?",(nombre, telefono, fecha_nac, id))
    conn.commit()
    conn.close()
    return redirect("/")
@app.route("/delete/<int:id>")
def persona_delete(id):
    conn = sqlite3.connect("kardex.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)
    