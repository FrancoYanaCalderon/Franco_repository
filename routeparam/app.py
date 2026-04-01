from flask import Flask
app = Flask(__name__)
@app.route("/usuario/<nombre>")
def perfil_usuario(nombre):
    return f"Perfil de: <strong>{nombre}</strong>"
@app.route("/post/<id>")
def ver_post(id):
    return f"Mostrando el post: <strong>{id}</strong>"
@app.route("/categoria/<categoria>/<productos>")
def productos(categoria, producto):
    return f"categoria: {categoria}, producto: {producto}"
if __name__ == "__main__":
    app.run(debug = True)