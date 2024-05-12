"""added hash contraseña column

Revision ID: 6762ed8eca3e
Revises: fa9d8d03f758
Create Date: 2024-05-11 21:01:14.373595

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6762ed8eca3e'
down_revision: Union[str, None] = 'fa9d8d03f758'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('oficiales', sa.Column('hash_contraseña', sa.String(60), unique=True, nullable=False))


def downgrade() -> None:
    pass
