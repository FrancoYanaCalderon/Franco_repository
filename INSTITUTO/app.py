import sqlite3

conn = sqlite3.connect("instituto.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    horas INTEGER NOT NULL
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_nacimineto DATE NOT NULL
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS inscripciones (
    id INTEGER PRIMARY KEY,
    fecha TEXT NOT NULL,
    curso_id INTEGER NOT NULL,
    estudiante_id INTEGER NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos (id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id)
    
)
""")


#Añadir 2 cursos
# conn.execute("""
#     INSERT INTO cursos (descripcion, horas)
#     VALUES ('Python de cero a experto', 20)


# """)

# conn.execute("""
#     INSERT INTO estudiantes (nombre, apellidos, fecha_nacimineto)
#     VALUES ('Franco', 'Yana', '1980-12-20')
# """)


conn.commit()

print("\nCURSOS")
cursor = conn.execute("SELECT * FROM cursos")
for row in cursor:
    print(row)

print("\nESTUDIANTES")
cursor = conn.execute("SELECT * FROM estudiantes")
for fila in cursor:
    print(fila)
    
print("\nINSCRIPCIONES")
cursor = conn.execute("SELECT * FROM inscripciones")
for fila in cursor:
    print(fila)