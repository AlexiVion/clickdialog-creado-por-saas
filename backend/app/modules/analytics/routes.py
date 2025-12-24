from flask import Blueprint, jsonify
from .models import Event

bp = Blueprint("analytics", __name__, url_prefix="/api/analytics")

@bp.get("/summary")
def summary():
    total = Event.query.count()
    return jsonify({"ok": True, "data": {"events_total": total}})
