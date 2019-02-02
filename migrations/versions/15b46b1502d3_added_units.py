"""added_units

Revision ID: 15b46b1502d3
Revises: 3a532c08bf79
Create Date: 2019-02-02 14:36:40.479809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15b46b1502d3'
down_revision = '3a532c08bf79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('units',
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('e_unit_name', sa.String(length=255), nullable=True),
    sa.Column('u_department', sa.String(length=255), nullable=True),
    sa.Column('u_unit', sa.String(length=255), nullable=True),
    sa.Column('u_ntt', sa.Integer(), nullable=True),
    sa.Column('u_tl_tenure', sa.Integer(), nullable=True),
    sa.Column('u_tl_age', sa.Integer(), nullable=True),
    sa.Column('u_tl_gender', sa.Integer(), nullable=True),
    sa.Column('u_hires_week', sa.Integer(), nullable=True),
    sa.Column('u_exits_week', sa.Integer(), nullable=True),
    sa.Column('u_hires_month', sa.Integer(), nullable=True),
    sa.Column('u_exits_month', sa.Integer(), nullable=True),
    sa.Column('u_headcount', sa.Integer(), nullable=True),
    sa.Column('u_age_mean', sa.Float(), nullable=True),
    sa.Column('u_tenure_mean', sa.Float(), nullable=True),
    sa.Column('u_gender_average', sa.Float(), nullable=True),
    sa.Column('u_tl_active', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('u_id')
    )
    op.add_column('candidate_predictions', sa.Column('e_unit_name', sa.String(length=255), nullable=True))
    op.add_column('candidate_predictions', sa.Column('u_unit_name', sa.String(length=255), nullable=True))
    op.drop_column('candidate_predictions', 'u_unit')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('candidate_predictions', sa.Column('u_unit', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('candidate_predictions', 'u_unit_name')
    op.drop_column('candidate_predictions', 'e_unit_name')
    op.drop_table('units')
    # ### end Alembic commands ###