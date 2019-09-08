"""create table delivery

Revision ID: b073df60e97b
Revises: 7b47983c2ea0
Create Date: 2019-09-08 10:37:51.647579

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b073df60e97b'
down_revision = '7b47983c2ea0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('delivery',
                    sa.Column('uid',
                              sa.String(36),
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False),
                    sa.Column('value',
                              sa.Float,
                              nullable=False))


def downgrade():
    op.drop_table('delivery')
