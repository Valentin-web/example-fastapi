"""add last few columns to post table

Revision ID: 23577863a309
Revises: 4f603841490d
Create Date: 2022-08-01 11:10:51.630282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23577863a309'
down_revision = '4f603841490d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
