"""Initial migration.

Revision ID: 31e318d505ae
Revises: 
Create Date: 2020-12-24 14:44:44.823728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31e318d505ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('warrant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('warrant', sa.String(), nullable=False),
    sa.Column('initial_warrant', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('warrant')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('warrant')
    # ### end Alembic commands ###