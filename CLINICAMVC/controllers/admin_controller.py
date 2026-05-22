from flask import request, redirect, url_for, Blueprint, session, flash
from models.usuario_model import Usuario
from models.medico_model import Medico
from models.paciente_model import Paciente
from models.consulta_model import Consulta
from views import admin_view
from functools import wraps

admin_bp = Blueprint('admin', __name__, url_prefix="/admin")


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Debes iniciar sesión para acceder.', 'warning')
            return redirect(url_for('auth.login'))
        if session.get('usuario_rol') != 'admin':
            flash('No tienes permisos para acceder al panel administrativo.', 'danger')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated


@admin_bp.route("/")
@admin_required
def panel():
    # Panel con estadisticas generales
    total_medicos = len(Medico.get_all())
    total_pacientes = len(Paciente.get_all())
    total_consultas = len(Consulta.get_all())
    total_usuarios = len(Usuario.get_all())
    ultimas_consultas = Consulta.get_all()[:5]
    return admin_view.panel(total_medicos, total_pacientes, total_consultas, total_usuarios, ultimas_consultas)


@admin_bp.route("/usuarios")
@admin_required
def usuarios():
    usuarios = Usuario.get_all()
    return admin_view.list_usuarios(usuarios)


@admin_bp.route("/usuarios/edit/<int:id>", methods=['GET', 'POST'])
@admin_required
def edit_usuario(id):
    usuario = Usuario.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form.get('password', '')
        rol = request.form['rol']
        usuario.update(nombre=nombre, username=username, password=password if password else None, rol=rol)
        flash('Usuario actualizado correctamente.', 'success')
        return redirect(url_for('admin.usuarios'))
    return admin_view.edit_usuario(usuario)


@admin_bp.route("/usuarios/delete/<int:id>")
@admin_required
def delete_usuario(id):
    # No permitir eliminar el propio usuario
    if session.get('usuario_id') == id:
        flash('No puedes eliminar tu propio usuario.', 'danger')
        return redirect(url_for('admin.usuarios'))
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    flash('Usuario eliminado.', 'danger')
    return redirect(url_for('admin.usuarios'))
