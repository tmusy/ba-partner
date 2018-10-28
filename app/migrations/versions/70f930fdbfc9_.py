"""empty message

Revision ID: 70f930fdbfc9
Revises: 3707f1d01aa2
Create Date: 2018-10-28 14:30:10.068844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70f930fdbfc9'
down_revision = '3707f1d01aa2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('partner', sa.Column('atk', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('cr', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('crd', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('df', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('hit', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('hp', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('leader_skill', sa.String(length=1080), nullable=True))
    op.add_column('partner', sa.Column('res', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('skill_1', sa.String(length=1080), nullable=True))
    op.add_column('partner', sa.Column('skill_2', sa.String(length=1080), nullable=True))
    op.add_column('partner', sa.Column('skill_3', sa.String(length=1080), nullable=True))
    op.add_column('partner', sa.Column('spd', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('tier', sa.Integer(), nullable=False))
    op.add_column('partner', sa.Column('type', sa.String(length=8), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('partner', 'type')
    op.drop_column('partner', 'tier')
    op.drop_column('partner', 'spd')
    op.drop_column('partner', 'skill_3')
    op.drop_column('partner', 'skill_2')
    op.drop_column('partner', 'skill_1')
    op.drop_column('partner', 'res')
    op.drop_column('partner', 'leader_skill')
    op.drop_column('partner', 'hp')
    op.drop_column('partner', 'hit')
    op.drop_column('partner', 'df')
    op.drop_column('partner', 'crd')
    op.drop_column('partner', 'cr')
    op.drop_column('partner', 'atk')
    # ### end Alembic commands ###
