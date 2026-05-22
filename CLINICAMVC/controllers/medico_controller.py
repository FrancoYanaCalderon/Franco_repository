from flask import request, redirect, url_for, Blueprint, session, flash
from models.medico_model import Medico
from views import medico_view
from functools import wraps

medico_bp = Blueprint('medicos', __name__, url_prefix="/medicos")


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Debes iniciar sesión para acceder.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated


@medico_bp.route("/")
@login_required
def index():
    medicos = Medico.get_all()
    return medico_view.list(medicos)


@medico_bp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']

        medico = Medico(nombre, especialidad, telefono, correo)
        medico.save()
        flash('Médico registrado correctamente.', 'success')
        return redirect(url_for('medicos.index'))

    return medico_view.create()


@medico_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    medico = Medico.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']

        medico.update(nombre=nombre, especialidad=especialidad, telefono=telefono, correo=correo)
        flash('Médico actualizado correctamente.', 'success')
        return redirect(url_for('medicos.index'))

    return medico_view.edit(medico)


@medico_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    medico = Medico.get_by_id(id)
    medico.delete()
    flash('Médico eliminado.', 'danger')
    return redirect(url_for('medicos.index'))
