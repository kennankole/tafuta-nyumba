"""empty message

Revision ID: 477a4f953b30
Revises: c464a71656d8
Create Date: 2022-03-13 11:41:09.178475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '477a4f953b30'
down_revision = 'c464a71656d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hostels_photo_gallery')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hostels_photo_gallery',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('image', sa.VARCHAR(length=20), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('image')
    )
    # ### end Alembic commands ###
