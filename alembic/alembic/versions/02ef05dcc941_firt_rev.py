"""firt rev

Revision ID: 02ef05dcc941
Revises: 
Create Date: 2024-05-10 18:39:05.047152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02ef05dcc941'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'persona',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String(100), nullable=False),
        sa.Column('correo_electronico', sa.String(255), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table('persona')