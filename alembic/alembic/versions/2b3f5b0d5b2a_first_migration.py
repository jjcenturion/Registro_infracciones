"""first migration

Revision ID: 2b3f5b0d5b2a
Revises: 
Create Date: 2024-05-09 17:35:56.625240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b3f5b0d5b2a'
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
