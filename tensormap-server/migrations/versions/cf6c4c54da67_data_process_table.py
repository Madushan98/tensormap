"""data process table

Revision ID: cf6c4c54da67
Revises: 8fc4a730f13b
Create Date: 2021-05-21 23:15:09.573973

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "cf6c4c54da67"
down_revision = "8fc4a730f13b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("data_file", sa.Column("created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True))
    op.add_column("data_file", sa.Column("updated_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True))
    op.alter_column("data_file", "file_name", existing_type=mysql.VARCHAR(length=100), nullable=False)
    op.alter_column("data_file", "file_type", existing_type=mysql.VARCHAR(length=10), nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("data_file", "file_type", existing_type=mysql.VARCHAR(length=10), nullable=True)
    op.alter_column("data_file", "file_name", existing_type=mysql.VARCHAR(length=100), nullable=True)
    op.drop_column("data_file", "updated_on")
    op.drop_column("data_file", "created_on")
    # ### end Alembic commands ###
