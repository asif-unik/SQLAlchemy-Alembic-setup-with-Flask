"""address

Revision ID: 7fbaa8321989
Revises: f11a1efd90c0
Create Date: 2024-05-30 12:12:57.924879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fbaa8321989'
down_revision: Union[str, None] = 'f11a1efd90c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("address",
                    sa.Column("id",sa.Integer(),nullable=False),
                    sa.Column("area",sa.String(),nullable=False),
                    sa.Column("city",sa.String(),nullable=False),
                    sa.Column("state",sa.String(),nullable=False),
                    sa.Column("pincode",sa.String(),nullable=False),
                    sa.Column("user_id",sa.Integer(),nullable=False),
                    sa.ForeignKeyConstraint(
                        ["user_id"],["user.id"],name="address_user_id_fkey",ondelete = "CASCADE"),
                    sa.PrimaryKeyConstraint("id"),
                    )


def downgrade() -> None:
    op.drop_table("address")


