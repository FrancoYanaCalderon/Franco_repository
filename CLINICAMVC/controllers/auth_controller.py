from flask import request, redirect, url_for, Blueprint, session, flash
from models.usuario_model import Usuario
from views import auth_view

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if 'usuario_id' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        usuario = Usuario.get_by_username(username)
        if usuario and usuario.verify_password(password):
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            session['usuario_rol'] = usuario.rol
            flash(f'Bienvenido, {usuario.nombre}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')

    return auth_view.login()


@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form.get('rol', 'enfermero')

        existente = Usuario.get_by_username(username)
        if existente:
            flash('El nombre de usuario ya existe.', 'danger')
            return auth_view.register()

        usuario = Usuario(nombre, username, password, rol)
        usuario.save()
        flash('Usuario registrado. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))

    return auth_view.register()


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('auth.login'))
