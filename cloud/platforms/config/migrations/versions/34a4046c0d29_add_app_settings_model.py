"""
Add app setting model
"""

import sqlalchemy as sa
from alembic import op

revision = "34a4046c0d29"
down_revision = "733b55f7f867"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "app_settings",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("key", sa.String(length=150), nullable=False),
        sa.Column("value", sa.String(length=150), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )


def downgrade() -> None:
    op.drop_table("app_settings")
