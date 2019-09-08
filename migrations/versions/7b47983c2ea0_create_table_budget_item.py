"""create table budget_item

Revision ID: 7b47983c2ea0
Revises: 89794c69ffab
Create Date: 2019-09-07 11:46:49.554912

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '7b47983c2ea0'
down_revision = '89794c69ffab'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('budget_item',
                    sa.Column('uid',
                              sa.String(36),
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False),
                    sa.Column('quantity',
                              sa.Integer,
                              nullable=False),
                    sa.Column('price',
                              sa.Float,
                              nullable=False),
                    sa.Column('total',
                              sa.Float,
                              nullable=False),
                    sa.Column('budget_uid',
                              sa.String(36),
                              sa.ForeignKey('budget.uid'),
                              nullable=False))


def downgrade():
    op.drop_table('budget_item')
