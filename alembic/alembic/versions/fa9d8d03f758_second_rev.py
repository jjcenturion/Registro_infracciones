"""second rev

Revision ID: fa9d8d03f758
Revises: 02ef05dcc941
Create Date: 2024-05-10 18:45:10.511304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa9d8d03f758'
down_revision: Union[str, None] = '02ef05dcc941'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'personas',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String(length=100), nullable=False),
        sa.Column('correo_electronico', sa.String(length=255), nullable=False, unique=True),
    )

    
    op.create_table(
        'vehiculos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('placa_patente', sa.String(length=20), nullable=False, unique=True),
        sa.Column('marca', sa.String(length=50)),
        sa.Column('color', sa.String(length=50)),
        sa.Column('propietario_id', sa.Integer, sa.ForeignKey('personas.id'))
    )

  
    op.create_table(
        'infracciones',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('placa_patente', sa.String(length=20), sa.ForeignKey('vehiculos.placa_patente'), nullable=False),
        sa.Column('timestamp', sa.DateTime, nullable=False),
        sa.Column('comentario', sa.Text)
    )

    op.create_table(
        'oficiales',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String(length=100), nullable=False),
        sa.Column('numero_identificatorio', sa.String(length=255), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table('infracciones')
    op.drop_table('vehiculos')
    op.drop_table('personas')
    op.drop_table('oficiales')