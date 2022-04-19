"""'add_common_index'

Revision ID: d61fb722c731
Revises: 74d72d87c72c
Create Date: 2022-03-20 20:18:42.804736

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd61fb722c731'
down_revision = '74d72d87c72c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index(
        index_name='expression_index',
        table_name='operations',
        columns=['operator', 'number1', 'number2'],
    )


def downgrade():
    op.drop_index(
        index_name='expression_index',
        table_name='operations'
    )
