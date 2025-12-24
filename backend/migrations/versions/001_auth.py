"""auth tables"""
from alembic import op
import sqlalchemy as sa

revision = "001_auth"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "tenants",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tenant_id", sa.Integer(), nullable=True),
        sa.Column("email", sa.String(length=180), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=64), nullable=False),
    )
    op.create_index("ix_roles_name", "roles", ["name"], unique=True)
    op.create_table(
        "user_roles",
        sa.Column("user_id", sa.Integer(), primary_key=True),
        sa.Column("role_id", sa.Integer(), primary_key=True),
    )

def downgrade():
    op.drop_table("user_roles")
    op.drop_index("ix_roles_name", table_name="roles")
    op.drop_table("roles")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
    op.drop_table("tenants")
