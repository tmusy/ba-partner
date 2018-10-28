"""empty message

Revision ID: 39fc9b1ea3c9
Revises: 70f930fdbfc9
Create Date: 2018-10-28 14:33:02.104604

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
import csv


# revision identifiers, used by Alembic.
revision = '39fc9b1ea3c9'
down_revision = '70f930fdbfc9'
branch_labels = None
depends_on = None


# Create an ad-hoc table to use for the insert statement.
partners_table = table('partner',
    column('id', sa.Integer),
    column('name', sa.String),
    column('color', sa.String),
    column('stars', sa.Integer),
    column('hp', sa.Integer),
    column('df', sa.Integer),
    column('atk', sa.Integer),
    column('spd', sa.Integer),
    column('cr', sa.Integer),
    column('crd', sa.Integer),
    column('res', sa.Integer),
    column('hit', sa.Integer),
    column('skill_1', sa.String),
    column('skill_2', sa.String),
    column('skill_3', sa.String),
    column('leader_skill', sa.String),
    column('tier', sa.Integer),
    column('type', sa.String),
)

data = []

with open('./PatternCompare.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 1
    for row in reader:
        data.append({
            'id': i,
            'name': row['name'],
            'stars': row['Stars'],
            'hp': row['HP'],
            'atk': row['ATK'],
            'df': row['DEF'],
            'spd': row['SPD'],
            'cr': row['CR'],
            'crd': row['CRD'],
            'res': row['RES'],
            'hit': row['HIT'],
            'color': row['color'],
            'type': row['type'],
            'leader_skill': row['Leader Skill'],
            'tier': row['Tier'],
            })

        i += 1


def upgrade():
    op.bulk_insert(partners_table, data)


def downgrade():
    pass
