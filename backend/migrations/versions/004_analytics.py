"""analytics tables"""
from alembic import op
import sqlalchemy as sa

revision = "004_analytics"
down_revision = '003_chatbot'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tenant_id", sa.Integer(), nullable=True),
        sa.Column("client_id", sa.String(length=120), nullable=True),
        sa.Column("name", sa.String(length=180), nullable=False),
        sa.Column("payload", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_events_name", "events", ["name"], unique=False)

def downgrade():
    op.drop_index("ix_events_name", table_name="events")
    op.drop_table("events")
