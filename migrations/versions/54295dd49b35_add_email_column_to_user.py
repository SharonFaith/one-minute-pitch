"""Add Email Column To User

Revision ID: 54295dd49b35
Revises: 2722dfd74c5c
Create Date: 2020-10-22 22:37:50.898017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54295dd49b35'
down_revision = '2722dfd74c5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
