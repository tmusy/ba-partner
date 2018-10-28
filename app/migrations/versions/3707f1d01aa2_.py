"""empty message

Revision ID: 3707f1d01aa2
Revises: cd540db6096e
Create Date: 2018-10-28 10:45:48.495147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3707f1d01aa2'
down_revision = 'cd540db6096e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('partner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('partner')
    # ### end Alembic commands ###