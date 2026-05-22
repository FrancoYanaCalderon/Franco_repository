from flask import render_template


def panel(total_medicos, total_pacientes, total_consultas, total_usuarios, ultimas_consultas):
    return render_template('usuario/panel.html',
                           total_medicos=total_medicos,
                           total_pacientes=total_pacientes,
                           total_consultas=total_consultas,
                           total_usuarios=total_usuarios,
                           ultimas_consultas=ultimas_consultas)


def list_usuarios(usuarios):
    return render_template('usuario/index.html', usuarios=usuarios)


def edit_usuario(usuario):
    return render_template('usuario/edit.html', usuario=usuario)
