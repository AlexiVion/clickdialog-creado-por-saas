from datetime import datetime
from app.extensions import db

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, nullable=True, index=True)
    client_id = db.Column(db.String(120), nullable=True, index=True)
    name = db.Column(db.String(180), nullable=False)  # e.g. landing.view, chatbot.message
    payload = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
