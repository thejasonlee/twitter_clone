"""empty message

Revision ID: 029b97c324be
Revises: 
Create Date: 2020-11-19 15:19:49.367086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '029b97c324be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_post_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_post'))
    )
    op.create_table('like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name=op.f('fk_like_post_id_post')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_like_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_like'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like')
    op.drop_table('post')
    op.drop_table('user')
    # ### end Alembic commands ###