"""empty message

Revision ID: 0a99f275b0d3
Revises: 2f1ec6d6f521
Create Date: 2024-02-22 00:24:56.286950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a99f275b0d3'
down_revision = '2f1ec6d6f521'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('base_hp', sa.Integer(), nullable=True),
    sa.Column('base_attack', sa.Integer(), nullable=True),
    sa.Column('base_defense', sa.Integer(), nullable=True),
    sa.Column('sprite_img', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
