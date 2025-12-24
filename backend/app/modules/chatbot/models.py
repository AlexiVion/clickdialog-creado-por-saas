from datetime import datetime
from app.extensions import db

class ChatThread(db.Model):
    __tablename__ = "chat_threads"
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, nullable=True, index=True)
    client_id = db.Column(db.String(120), nullable=True, index=True)
    channel = db.Column(db.String(64), nullable=False, default="webchat")  # webchat|whatsapp|...
    session_id = db.Column(db.String(180), nullable=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ChatMessage(db.Model):
    __tablename__ = "chat_messages"
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey("chat_threads.id"), nullable=False, index=True)
    role = db.Column(db.String(20), nullable=False)  # user|assistant|system
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
