"""bigbang

Revision ID: 06b383447f6a
Revises: 
Create Date: 2024-01-18 15:07:35.705755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06b383447f6a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('MegaSena',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('concursos_id', sa.Integer(), nullable=False),
    sa.Column('MegaSena_virada', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('concursos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('concurso', sa.Integer(), nullable=False),
    sa.Column('data_sorteio', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('concursos')
    op.drop_table('MegaSena')
    # ### end Alembic commands ###
