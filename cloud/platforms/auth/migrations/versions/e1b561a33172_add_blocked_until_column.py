"""
Add blocked until column
"""

import sqlalchemy as sa
from alembic import op

revision = "e1b561a33172"
down_revision = "704b9ed54608"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("locked_until", sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "locked_until")
