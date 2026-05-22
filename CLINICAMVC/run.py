from flask import Flask, redirect, url_for, session
from controllers import medico_controller
from controllers import paciente_controller
from controllers import consulta_controller
from controllers import auth_controller
from controllers import admin_controller
from models.medico_model import Medico
from models.paciente_model import Paciente
from models.consulta_model import Consulta
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "clinica-mvc-secret-2026"

db.init_app(app)

app.register_blueprint(medico_controller.medico_bp)
app.register_blueprint(paciente_controller.paciente_bp)
app.register_blueprint(consulta_controller.consulta_bp)
app.register_blueprint(auth_controller.auth_bp)
app.register_blueprint(admin_controller.admin_bp)


@app.route("/")
def home():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    total_medicos = len(Medico.get_all())
    total_pacientes = len(Paciente.get_all())
    total_consultas = len(Consulta.get_all())
    ultimas_consultas = Consulta.get_all()[:5]

    from flask import render_template
    return render_template('home.html',
                           total_medicos=total_medicos,
                           total_pacientes=total_pacientes,
                           total_consultas=total_consultas,
                           ultimas_consultas=ultimas_consultas)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
