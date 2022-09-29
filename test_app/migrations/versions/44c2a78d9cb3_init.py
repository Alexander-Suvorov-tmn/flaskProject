"""init

Revision ID: 44c2a78d9cb3
Revises: 
Create Date: 2022-09-27 14:30:40.095038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44c2a78d9cb3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order', sa.BigInteger(), nullable=True),
    sa.Column('price', sa.BigInteger(), nullable=True),
    sa.Column('price_rus', sa.Float(), nullable=True),
    sa.Column('delivery_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_data_order'), 'order_data', ['order'], unique=True)
    op.create_index(op.f('ix_order_data_price'), 'order_data', ['price'], unique=False)
    op.create_index(op.f('ix_order_data_price_rus'), 'order_data', ['price_rus'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_data_price_rus'), table_name='order_data')
    op.drop_index(op.f('ix_order_data_price'), table_name='order_data')
    op.drop_index(op.f('ix_order_data_order'), table_name='order_data')
    op.drop_table('order_data')
    # ### end Alembic commands ###