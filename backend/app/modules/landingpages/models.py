from datetime import datetime
from app.extensions import db

class LandingPage(db.Model):
    __tablename__ = "landing_pages"
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, nullable=True, index=True)
    client_id = db.Column(db.String(120), nullable=True, index=True)

    slug = db.Column(db.String(240), nullable=False, unique=True)
    business_name = db.Column(db.String(240), nullable=True)
    html_path = db.Column(db.String(500), nullable=True)  # opcional: path local/objeto
    meta_json = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
