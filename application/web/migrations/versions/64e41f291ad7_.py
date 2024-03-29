"""empty message

Revision ID: 64e41f291ad7
Revises: 4779a0bb030e
Create Date: 2022-03-15 16:20:26.014126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64e41f291ad7'
down_revision = '4779a0bb030e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assets',
    sa.Column('user_Id', sa.INTEGER(), nullable=False),
    sa.Column('hostels_id', sa.INTEGER(), nullable=False),
    sa.Column('houses_id', sa.INTEGER(), nullable=False),
    sa.Column('business_premises_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['business_premises_id'], ['business_premises.id'], ),
    sa.ForeignKeyConstraint(['hostels_id'], ['hostels.id'], ),
    sa.ForeignKeyConstraint(['houses_id'], ['houses.id'], ),
    sa.ForeignKeyConstraint(['user_Id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_Id', 'hostels_id', 'houses_id', 'business_premises_id')
    )
    # ### end Alembic commands ###
