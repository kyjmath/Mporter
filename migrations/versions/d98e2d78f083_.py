"""empty message

Revision ID: d98e2d78f083
Revises: 
Create Date: 2018-07-22 12:36:06.291021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd98e2d78f083'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mentees', sa.Column('mentee_email', sa.String(length=256), nullable=True))
    op.create_unique_constraint(None, 'mentees', ['mentee_email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mentees', type_='unique')
    op.drop_column('mentees', 'mentee_email')
    # ### end Alembic commands ###
