"""user

Revision ID: f11a1efd90c0
Revises: 
Create Date: 2024-05-30 11:50:02.786979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f11a1efd90c0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # op.create_table('users',
                    # sa.Column('id',sa.Integer,primary_key=True),
                    # sa.Column('name',sa.String(50),nullable=False),
                    # sa.Column('email',sa.String(100), nullable=False),
                    # sa.Column('age', sa.Integer(), nullable=True),
                    # sa.PrimaryKeyConstraint('id'))


def downgrade() -> None:
    op.drop_table('users')
