"""migracion inicial

Revision ID: 22d76bd4ee29
Revises: 
Create Date: 2026-05-26 20:19:35.137064

"""
from alembic import op
import sqlalchemy as sa

revision = '22d76bd4ee29'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('clientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('telefono', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('productos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.Column('monto', sa.Float(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('pedidos')
    op.drop_table('productos')
    op.drop_table('clientes')

