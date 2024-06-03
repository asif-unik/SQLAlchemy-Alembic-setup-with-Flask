"""add country table in address

Revision ID: ac0df7c2e43c
Revises: 0defb10491c5
Create Date: 2024-05-30 20:19:51.655394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac0df7c2e43c'
down_revision: Union[str, None] = '0defb10491c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('address', sa.Column('country', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'country')
