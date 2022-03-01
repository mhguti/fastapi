"""add content column

Revision ID: c18389995c05
Revises: afbe92869aec
Create Date: 2022-02-27 23:08:49.500962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c18389995c05'
down_revision = 'afbe92869aec'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
