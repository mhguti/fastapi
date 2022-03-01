import sqlalchemy as sa
"""create posts table

Revision ID: afbe92869aec
Revises: 
Create Date: 2022-02-27 22:58:00.037873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afbe92869aec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable = False))

    pass


def downgrade():
    op.drop_table('posts')
    pass
