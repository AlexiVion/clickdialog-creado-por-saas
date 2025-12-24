"""integration tables"""
from alembic import op
import sqlalchemy as sa

revision = "005_integration"
down_revision = '004_analytics'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "landing_chat_tracking",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("landing_page_id", sa.Integer(), nullable=False),
        sa.Column("chat_thread_id", sa.Integer(), nullable=False),
        sa.Column("event", sa.String(length=120), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_lct_landing_page_id", "landing_chat_tracking", ["landing_page_id"], unique=False)
    op.create_index("ix_lct_chat_thread_id", "landing_chat_tracking", ["chat_thread_id"], unique=False)

def downgrade():
    op.drop_index("ix_lct_chat_thread_id", table_name="landing_chat_tracking")
    op.drop_index("ix_lct_landing_page_id", table_name="landing_chat_tracking")
    op.drop_table("landing_chat_tracking")
