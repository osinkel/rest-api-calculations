"""create operations table

Revision ID: 74d72d87c72c
Revises: 
Create Date: 2022-03-17 18:42:18.342353

"""
from alembic import op
import sqlalchemy as sa
from db.models.operation import allowed_operations


# revision identifiers, used by Alembic.
revision = '74d72d87c72c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('operations',
                    sa.Column('id', sa.Integer),
                    sa.Column('operator', sa.Enum(allowed_operations)),
                    sa.Column('number1', sa.Numeric),
                    sa.Column('number2', sa.Numeric),
                    sa.Column('result', sa.Numeric),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Index('idx_operator', 'operator'),
                    sa.Index('idx_result', 'result'),
                    )


def downgrade():
    op.drop_index('idx_operator', table_name='operations')
    op.drop_index('idx_result', table_name='operations')
    op.drop_table('operations')
