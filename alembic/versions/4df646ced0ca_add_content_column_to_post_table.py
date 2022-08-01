"""add content column to post table

Revision ID: 4df646ced0ca
Revises: 9c17c1403ef8
Create Date: 2022-08-01 10:42:59.799437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4df646ced0ca'
down_revision = '9c17c1403ef8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
