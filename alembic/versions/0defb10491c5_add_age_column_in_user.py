"""add age column in user

Revision ID: 0defb10491c5
Revises: 7fbaa8321989
Create Date: 2024-05-30 15:46:44.189256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0defb10491c5'
down_revision: Union[str, None] = '7fbaa8321989'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'age')