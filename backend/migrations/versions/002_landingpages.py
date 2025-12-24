"""landingpages tables"""
from alembic import op
import sqlalchemy as sa

revision = "002_landingpages"
down_revision = '001_auth'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "landing_pages",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("tenant_id", sa.Integer(), nullable=True),
        sa.Column("client_id", sa.String(length=120), nullable=True),
        sa.Column("slug", sa.String(length=240), nullable=False),
        sa.Column("business_name", sa.String(length=240), nullable=True),
        sa.Column("html_path", sa.String(length=500), nullable=True),
        sa.Column("meta_json", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_landing_pages_slug", "landing_pages", ["slug"], unique=True)
    op.create_index("ix_landing_pages_client_id", "landing_pages", ["client_id"], unique=False)

def downgrade():
    op.drop_index("ix_landing_pages_client_id", table_name="landing_pages")
    op.drop_index("ix_landing_pages_slug", table_name="landing_pages")
    op.drop_table("landing_pages")
