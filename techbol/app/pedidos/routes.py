from flask import request, render_template, redirect, url_for, Blueprint
from app import db
from app.pedidos.models import Pedido
from app.clientes.models import Cliente
from app.productos.models import Producto

bp_pedidos = Blueprint('bp_pedidos', __name__, template_folder='templates')

@bp_pedidos.route("/")
def index():
    pedidos = Pedido.query.all()
    return render_template('pedidos/index.html', pedidos=pedidos)

@bp_pedidos.route("/create", methods=['GET', 'POST'])
def create():
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    if request.method == 'GET':
        return render_template('pedidos/create.html', clientes=clientes, productos=productos)
    elif request.method == 'POST':
        monto = float(request.form.get('monto'))
        producto_id = int(request.form.get('producto_id'))
        cliente_id = int(request.form.get('cliente_id'))
        pedido = Pedido(monto=monto, producto_id=producto_id, cliente_id=cliente_id)
        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for('bp_pedidos.index'))

@bp_pedidos.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    pedido = Pedido.query.get_or_404(id)
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    if request.method == 'GET':
        return render_template('pedidos/edit.html', pedido=pedido, clientes=clientes, productos=productos)
    elif request.method == 'POST':
        pedido.monto = float(request.form.get('monto'))
        pedido.producto_id = int(request.form.get('producto_id'))
        pedido.cliente_id = int(request.form.get('cliente_id'))
        db.session.commit()
        return redirect(url_for('bp_pedidos.index'))

@bp_pedidos.route("/delete/<int:id>", methods=['POST'])
def delete(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('bp_pedidos.index'))
