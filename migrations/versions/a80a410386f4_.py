"""empty message

Revision ID: a80a410386f4
Revises: 
Create Date: 2020-11-17 19:11:37.926124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a80a410386f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('code', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('currency_rate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.Column('time_from', sa.DateTime(), nullable=True),
    sa.Column('time_before', sa.DateTime(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('currency_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currency_rate')
    op.drop_table('currency')
    # ### end Alembic commands ###
