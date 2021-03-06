"""Add Passsecure Column

Revision ID: 2722dfd74c5c
Revises: 82ccabc768dd
Create Date: 2020-10-22 22:01:08.166454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2722dfd74c5c'
down_revision = '82ccabc768dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
