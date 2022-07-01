"""create profile and subscription tables

Revision ID: 26454e725a3a
Revises: 
Create Date: 2022-06-30 23:12:27.018171

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '26454e725a3a'
down_revision = None
branch_labels = None
depends_on = 'f327cd3f47ff'


def upgrade():
    op.create_table('profile',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('city', sa.String(), nullable=True),
                    sa.UniqueConstraint('user_id'),
                    sa.PrimaryKeyConstraint('id'),
                    )

    op.create_table('subscription',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('profile_id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
                    )


def downgrade():
    op.drop_table('subscription')
    op.drop_table('profile')
