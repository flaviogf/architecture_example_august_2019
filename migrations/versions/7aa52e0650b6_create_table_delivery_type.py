"""create table delivery_type

Revision ID: 7aa52e0650b6
Revises: 7b47983c2ea0
Create Date: 2019-09-07 11:56:05.231650

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '7aa52e0650b6'
down_revision = '7b47983c2ea0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('delivery_type',
                    sa.Column('name',
                              sa.String(250),
                              primary_key=True),
                    sa.Column('value',
                              sa.Float,
                              nullable=False))


def downgrade():
    op.drop_table('delivery_type')
