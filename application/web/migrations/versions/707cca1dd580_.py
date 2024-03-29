"""empty message

Revision ID: 707cca1dd580
Revises:
Create Date: 2021-09-26 11:06:57.822476


"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "707cca1dd580"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("land", schema=None) as batch_op:
        batch_op.drop_index("ix_land_alternate_contact")
        batch_op.drop_index("ix_land_area")
        batch_op.drop_index("ix_land_constituency")
        batch_op.drop_index("ix_land_contacts")
        batch_op.drop_index("ix_land_county")
        batch_op.drop_index("ix_land_plots")
        batch_op.drop_index("ix_land_price")
        batch_op.drop_index("ix_land_ward")

    op.drop_table("land")
    with op.batch_alter_table("hostels", schema=None) as batch_op:
        batch_op.drop_index("ix_hostels_alternate_contact")
        batch_op.drop_index("ix_hostels_constituency")
        batch_op.drop_index("ix_hostels_contacts")
        batch_op.drop_index("ix_hostels_county")
        batch_op.drop_index("ix_hostels_price")
        batch_op.drop_index("ix_hostels_school_name")
        batch_op.drop_index("ix_hostels_units")
        batch_op.drop_index("ix_hostels_ward")

    op.drop_table("hostels")
    with op.batch_alter_table("business_premise", schema=None) as batch_op:
        batch_op.drop_index("ix_business_premise_alternate_contact")
        batch_op.drop_index("ix_business_premise_area")
        batch_op.drop_index("ix_business_premise_constituency")
        batch_op.drop_index("ix_business_premise_contacts")
        batch_op.drop_index("ix_business_premise_county")
        batch_op.drop_index("ix_business_premise_price")
        batch_op.drop_index("ix_business_premise_street_name")
        batch_op.drop_index("ix_business_premise_type_of_business_premise")
        batch_op.drop_index("ix_business_premise_units")
        batch_op.drop_index("ix_business_premise_ward")

    op.drop_table("business_premise")
    with op.batch_alter_table("houses", schema=None) as batch_op:
        batch_op.drop_index("ix_houses_alternate_contact")
        batch_op.drop_index("ix_houses_constituency")
        batch_op.drop_index("ix_houses_contacts")
        batch_op.drop_index("ix_houses_county")
        batch_op.drop_index("ix_houses_name_of_estate_or_village")
        batch_op.drop_index("ix_houses_price")
        batch_op.drop_index("ix_houses_type_of_house")
        batch_op.drop_index("ix_houses_units")
        batch_op.drop_index("ix_houses_ward")

    op.drop_table("houses")
    with op.batch_alter_table("business_premises", schema=None) as batch_op:
        batch_op.drop_index("ix_business_premises_alternate_contact")
        batch_op.drop_index("ix_business_premises_area")
        batch_op.drop_index("ix_business_premises_constituency")
        batch_op.drop_index("ix_business_premises_contacts")
        batch_op.drop_index("ix_business_premises_county")
        batch_op.drop_index("ix_business_premises_price")
        batch_op.drop_index("ix_business_premises_street_name")
        batch_op.drop_index("ix_business_premises_type_of_business_premise")
        batch_op.drop_index("ix_business_premises_units")
        batch_op.drop_index("ix_business_premises_ward")

    op.drop_table("business_premises")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "business_premises",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("county", sa.VARCHAR(length=64), nullable=True),
        sa.Column("constituency", sa.VARCHAR(length=150), nullable=True),
        sa.Column("ward", sa.VARCHAR(length=150), nullable=True),
        sa.Column("street_name", sa.VARCHAR(length=254), nullable=True),
        sa.Column("type_of_business_premise", sa.INTEGER(), nullable=True),
        sa.Column("area", sa.INTEGER(), nullable=True),
        sa.Column("units", sa.INTEGER(), nullable=True),
        sa.Column("price", sa.INTEGER(), nullable=True),
        sa.Column("contacts", sa.VARCHAR(length=64), nullable=True),
        sa.Column("alternate_contact", sa.VARCHAR(length=64), nullable=True),
        sa.Column("for_rent", sa.BOOLEAN(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("business_premises", schema=None) as batch_op:
        batch_op.create_index("ix_business_premises_ward", ["ward"], unique=False)
        batch_op.create_index("ix_business_premises_units", ["units"], unique=False)
        batch_op.create_index(
            "ix_business_premises_type_of_business_premise",
            ["type_of_business_premise"],
            unique=False,
        )
        batch_op.create_index(
            "ix_business_premises_street_name", ["street_name"], unique=False
        )
        batch_op.create_index("ix_business_premises_price", ["price"], unique=False)
        batch_op.create_index("ix_business_premises_county", ["county"], unique=False)
        batch_op.create_index(
            "ix_business_premises_contacts", ["contacts"], unique=False
        )
        batch_op.create_index(
            "ix_business_premises_constituency", ["constituency"], unique=False
        )
        batch_op.create_index("ix_business_premises_area", ["area"], unique=False)
        batch_op.create_index(
            "ix_business_premises_alternate_contact",
            ["alternate_contact"],
            unique=False,
        )

    op.create_table(
        "houses",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("county", sa.VARCHAR(length=254), nullable=True),
        sa.Column("constituency", sa.VARCHAR(length=254), nullable=True),
        sa.Column("ward", sa.VARCHAR(length=150), nullable=True),
        sa.Column("name_of_estate_or_village", sa.VARCHAR(length=254), nullable=True),
        sa.Column("type_of_house", sa.VARCHAR(length=254), nullable=True),
        sa.Column("units", sa.INTEGER(), nullable=True),
        sa.Column("price", sa.INTEGER(), nullable=True),
        sa.Column("contacts", sa.VARCHAR(length=64), nullable=True),
        sa.Column("alternate_contact", sa.VARCHAR(length=64), nullable=True),
        sa.Column("for_rent", sa.BOOLEAN(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("houses", schema=None) as batch_op:
        batch_op.create_index("ix_houses_ward", ["ward"], unique=False)
        batch_op.create_index("ix_houses_units", ["units"], unique=False)
        batch_op.create_index(
            "ix_houses_type_of_house", ["type_of_house"], unique=False
        )
        batch_op.create_index("ix_houses_price", ["price"], unique=False)
        batch_op.create_index(
            "ix_houses_name_of_estate_or_village",
            ["name_of_estate_or_village"],
            unique=False,
        )
        batch_op.create_index("ix_houses_county", ["county"], unique=False)
        batch_op.create_index("ix_houses_contacts", ["contacts"], unique=False)
        batch_op.create_index("ix_houses_constituency", ["constituency"], unique=False)
        batch_op.create_index(
            "ix_houses_alternate_contact", ["alternate_contact"], unique=False
        )

    op.create_table(
        "business_premise",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("county", sa.VARCHAR(length=64), nullable=True),
        sa.Column("constituency", sa.VARCHAR(length=150), nullable=True),
        sa.Column("ward", sa.VARCHAR(length=150), nullable=True),
        sa.Column("street_name", sa.VARCHAR(length=254), nullable=True),
        sa.Column("type_of_business_premise", sa.INTEGER(), nullable=True),
        sa.Column("area", sa.INTEGER(), nullable=True),
        sa.Column("units", sa.INTEGER(), nullable=True),
        sa.Column("price", sa.INTEGER(), nullable=True),
        sa.Column("contacts", sa.VARCHAR(length=64), nullable=True),
        sa.Column("alternate_contact", sa.VARCHAR(length=64), nullable=True),
        sa.Column("for_rent", sa.BOOLEAN(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("business_premise", schema=None) as batch_op:
        batch_op.create_index("ix_business_premise_ward", ["ward"], unique=False)
        batch_op.create_index("ix_business_premise_units", ["units"], unique=False)
        batch_op.create_index(
            "ix_business_premise_type_of_business_premise",
            ["type_of_business_premise"],
            unique=False,
        )
        batch_op.create_index(
            "ix_business_premise_street_name", ["street_name"], unique=False
        )
        batch_op.create_index("ix_business_premise_price", ["price"], unique=False)
        batch_op.create_index("ix_business_premise_county", ["county"], unique=False)
        batch_op.create_index(
            "ix_business_premise_contacts", ["contacts"], unique=False
        )
        batch_op.create_index(
            "ix_business_premise_constituency", ["constituency"], unique=False
        )
        batch_op.create_index("ix_business_premise_area", ["area"], unique=False)
        batch_op.create_index(
            "ix_business_premise_alternate_contact", ["alternate_contact"], unique=False
        )

    op.create_table(
        "hostels",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("county", sa.VARCHAR(length=64), nullable=True),
        sa.Column("constituency", sa.VARCHAR(length=150), nullable=True),
        sa.Column("ward", sa.VARCHAR(length=150), nullable=True),
        sa.Column("school_name", sa.VARCHAR(length=150), nullable=True),
        sa.Column("units", sa.INTEGER(), nullable=True),
        sa.Column("price", sa.INTEGER(), nullable=True),
        sa.Column("contacts", sa.VARCHAR(length=64), nullable=True),
        sa.Column("alternate_contact", sa.VARCHAR(length=64), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("hostels", schema=None) as batch_op:
        batch_op.create_index("ix_hostels_ward", ["ward"], unique=False)
        batch_op.create_index("ix_hostels_units", ["units"], unique=False)
        batch_op.create_index("ix_hostels_school_name", ["school_name"], unique=False)
        batch_op.create_index("ix_hostels_price", ["price"], unique=False)
        batch_op.create_index("ix_hostels_county", ["county"], unique=False)
        batch_op.create_index("ix_hostels_contacts", ["contacts"], unique=False)
        batch_op.create_index("ix_hostels_constituency", ["constituency"], unique=False)
        batch_op.create_index(
            "ix_hostels_alternate_contact", ["alternate_contact"], unique=False
        )

    op.create_table(
        "land",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("county", sa.VARCHAR(length=64), nullable=True),
        sa.Column("constituency", sa.VARCHAR(length=150), nullable=True),
        sa.Column("ward", sa.VARCHAR(length=150), nullable=True),
        sa.Column("area", sa.INTEGER(), nullable=True),
        sa.Column("plots", sa.INTEGER(), nullable=True),
        sa.Column("price", sa.INTEGER(), nullable=True),
        sa.Column("contacts", sa.VARCHAR(length=64), nullable=True),
        sa.Column("alternate_contact", sa.VARCHAR(length=64), nullable=True),
        sa.Column("for_rent", sa.BOOLEAN(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("land", schema=None) as batch_op:
        batch_op.create_index("ix_land_ward", ["ward"], unique=False)
        batch_op.create_index("ix_land_price", ["price"], unique=False)
        batch_op.create_index("ix_land_plots", ["plots"], unique=False)
        batch_op.create_index("ix_land_county", ["county"], unique=False)
        batch_op.create_index("ix_land_contacts", ["contacts"], unique=False)
        batch_op.create_index("ix_land_constituency", ["constituency"], unique=False)
        batch_op.create_index("ix_land_area", ["area"], unique=False)
        batch_op.create_index(
            "ix_land_alternate_contact", ["alternate_contact"], unique=False
        )

    # ### end Alembic commands ###
