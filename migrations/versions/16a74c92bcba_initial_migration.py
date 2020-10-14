"""initial migration

Revision ID: 16a74c92bcba
Revises: 
Create Date: 2020-10-11 20:06:06.206964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16a74c92bcba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('content', sa.Text(), nullable=True))
    op.add_column('post', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('post', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.drop_column('post', 'message')
    op.drop_column('post', 'date')
    op.drop_column('post', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('username', sa.VARCHAR(length=50), nullable=False))
    op.add_column('post', sa.Column('date', sa.DATETIME(), nullable=False))
    op.add_column('post', sa.Column('message', sa.TEXT(), nullable=False))
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('post', 'timestamp')
    op.drop_column('post', 'id')
    op.drop_column('post', 'content')
    # ### end Alembic commands ###

# Create table User
# create attribute user_name as string, validation requirement 1, validation requirement 2
# create attribute password
#

# Create tweet
# Attribute body
# Attribute like count

# -----
# to tweet table, add attribute author