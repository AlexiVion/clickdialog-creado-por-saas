"""chatbot tables"""
from alembic import op
import sqlalchemy as sa

revision = "003_chatbot"
down_revision = '002_landingpages'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "chat_threads",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tenant_id", sa.Integer(), nullable=True),
        sa.Column("client_id", sa.String(length=120), nullable=True),
        sa.Column("channel", sa.String(length=64), nullable=False),
        sa.Column("session_id", sa.String(length=180), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_chat_threads_session_id", "chat_threads", ["session_id"], unique=False)
    op.create_table(
        "chat_messages",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("thread_id", sa.Integer(), nullable=False),
        sa.Column("role", sa.String(length=20), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_chat_messages_thread_id", "chat_messages", ["thread_id"], unique=False)

def downgrade():
    op.drop_index("ix_chat_messages_thread_id", table_name="chat_messages")
    op.drop_table("chat_messages")
    op.drop_index("ix_chat_threads_session_id", table_name="chat_threads")
    op.drop_table("chat_threads")
