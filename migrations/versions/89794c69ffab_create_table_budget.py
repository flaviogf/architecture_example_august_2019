"""create table budget

Revision ID: 89794c69ffab
Revises:
Create Date: 2019-09-07 11:41:56.428877

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '89794c69ffab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('budget',
                    sa.Column('uid',
                              sa.String(36),
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False),
                    sa.Column('email',
                              sa.String(250),
                              nullable=False),
                    sa.Column('phone',
                              sa.String(250),
                              nullable=False),
                    sa.Column('total',
                              sa.Float,
                              nullable=False))


def downgrade():
    op.drop_table('budget')
