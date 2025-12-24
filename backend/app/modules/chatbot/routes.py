from flask import Blueprint, request, jsonify
from app.extensions import db
from app.utils.errors import api_error
from .models import ChatThread, ChatMessage

bp = Blueprint("chatbot", __name__, url_prefix="/api/chatbot")

@bp.get("/threads")
def list_threads():
    items = ChatThread.query.order_by(ChatThread.created_at.desc()).limit(200).all()
    return jsonify({"ok": True, "data": [{
        "id": t.id,
        "channel": t.channel,
        "session_id": t.session_id,
        "created_at": t.created_at.isoformat()
    } for t in items]})

@bp.post("/messages")
def add_message():
    data = request.get_json(silent=True) or {}
    thread_id = data.get("thread_id")
    role = data.get("role")
    content = data.get("content")

    if not thread_id or not role or not content:
        return api_error("VALIDATION_ERROR", "Faltan campos (thread_id, role, content)", 400)

    if not ChatThread.query.get(int(thread_id)):
        return api_error("NOT_FOUND", "Thread no existe", 404)

    m = ChatMessage(thread_id=int(thread_id), role=str(role), content=str(content))
    db.session.add(m)
    db.session.commit()
    return jsonify({"ok": True, "data": {"id": m.id}}), 201

@bp.post("/threads")
def create_thread():
    data = request.get_json(silent=True) or {}
    t = ChatThread(
        tenant_id=data.get("tenant_id"),
        client_id=data.get("client_id"),
        channel=data.get("channel") or "webchat",
        session_id=data.get("session_id"),
    )
    db.session.add(t)
    db.session.commit()
    return jsonify({"ok": True, "data": {"id": t.id}}), 201
