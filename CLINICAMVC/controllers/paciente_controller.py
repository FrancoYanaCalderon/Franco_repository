from flask import request, redirect, url_for, Blueprint, session, flash
from models.paciente_model import Paciente
from models.consulta_model import Consulta
from views import paciente_view
from functools import wraps

paciente_bp = Blueprint('pacientes', __name__, url_prefix="/pacientes")


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Debes iniciar sesión para acceder.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated


@paciente_bp.route("/")
@login_required
def index():
    pacientes = Paciente.get_all()
    return paciente_view.list(pacientes)


@paciente_bp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        paciente = Paciente(nombre, edad, direccion, telefono)
        paciente.save()
        flash('Paciente registrado correctamente.', 'success')
        return redirect(url_for('pacientes.index'))

    return paciente_view.create()


@paciente_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    paciente = Paciente.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        paciente.update(nombre=nombre, edad=edad, direccion=direccion, telefono=telefono)
        flash('Paciente actualizado correctamente.', 'success')
        return redirect(url_for('pacientes.index'))

    return paciente_view.edit(paciente)


@paciente_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    paciente = Paciente.get_by_id(id)
    paciente.delete()
    flash('Paciente eliminado.', 'danger')
    return redirect(url_for('pacientes.index'))


@paciente_bp.route("/historial/<int:id>")
@login_required
def historial(id):
    # Extra: historial medico del paciente
    paciente = Paciente.get_by_id(id)
    consultas = Consulta.get_by_paciente(id)
    return paciente_view.historial(paciente, consultas)
