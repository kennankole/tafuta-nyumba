"""empty message

Revision ID: 73cd5d3731f8
Revises: 0fcac6ddc9a0
Create Date: 2022-03-29 17:12:22.840438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73cd5d3731f8'
down_revision = '0fcac6ddc9a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('business_assets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_unique_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('business_assets_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_unique_id'], ['unique_id'])
        batch_op.drop_column('user_id')

    with op.batch_alter_table('hostel_assets', schema=None) as batch_op:
        batch_op.drop_constraint('hostel_assets_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['unique_id'], ondelete='cascade')

    with op.batch_alter_table('house_assets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_unique_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('house_assets_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_unique_id'], ['unique_id'])
        batch_op.drop_column('user_id')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unique_id', sa.String(), autoincrement=False, nullable=False))
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('user_id_seq'::regclass)"), autoincrement=True, nullable=False))
        batch_op.drop_column('unique_id')

    with op.batch_alter_table('house_assets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('house_assets_user_id_fkey', 'user', ['user_id'], ['id'])
        batch_op.drop_column('user_unique_id')

    with op.batch_alter_table('hostel_assets', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('hostel_assets_user_id_fkey', 'user', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('business_assets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('business_assets_user_id_fkey', 'user', ['user_id'], ['id'])
        batch_op.drop_column('user_unique_id')

    # ### end Alembic commands ###
