from flask import request, redirect, url_for, Blueprint, session, flash
from datetime import datetime
from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente
from views import consulta_view
from functools import wraps

consulta_bp = Blueprint('consultas', __name__, url_prefix="/consultas")


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Debes iniciar sesión para acceder.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated


@consulta_bp.route("/")
@login_required
def index():
    # Extra: filtro por fecha
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        fi = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
        ff = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
        consultas = Consulta.get_by_fecha(fi, ff)
    else:
        consultas = Consulta.get_all()

    return consulta_view.list(consultas, fecha_inicio, fecha_fin)


@consulta_bp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        consulta = Consulta(fecha, diagnostico, tratamiento, id_medico, id_paciente)
        consulta.save()
        flash('Consulta registrada correctamente.', 'success')
        return redirect(url_for('consultas.index'))

    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    return consulta_view.create(medicos, pacientes)


@consulta_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    consulta = Consulta.get_by_id(id)
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        consulta.update(fecha=fecha, diagnostico=diagnostico, tratamiento=tratamiento,
                        id_medico=id_medico, id_paciente=id_paciente)
        flash('Consulta actualizada correctamente.', 'success')
        return redirect(url_for('consultas.index'))

    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    return consulta_view.edit(consulta, medicos, pacientes)


@consulta_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    consulta = Consulta.get_by_id(id)
    consulta.delete()
    flash('Consulta eliminada.', 'danger')
    return redirect(url_for('consultas.index'))
