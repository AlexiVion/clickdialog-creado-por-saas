from flask import Blueprint, request, jsonify
from app.extensions import db
from app.utils.errors import api_error
from .models import LandingPage

bp = Blueprint("landingpages", __name__, url_prefix="/api/landingpages")

@bp.get("")
def list_landingpages():
    items = LandingPage.query.order_by(LandingPage.created_at.desc()).limit(200).all()
    return jsonify({"ok": True, "data": [{
        "id": i.id,
        "slug": i.slug,
        "business_name": i.business_name,
        "created_at": i.created_at.isoformat()
    } for i in items]})

@bp.post("")
def create_landingpage():
    data = request.get_json(silent=True) or {}
    slug = (data.get("slug") or "").strip()
    if not slug:
        return api_error("VALIDATION_ERROR", "Falta slug", 400)

    if LandingPage.query.filter_by(slug=slug).first():
        return api_error("VALIDATION_ERROR", "Slug ya existe", 400)

    lp = LandingPage(
        tenant_id=data.get("tenant_id"),
        client_id=data.get("client_id"),
        slug=slug,
        business_name=data.get("business_name"),
        html_path=data.get("html_path"),
        meta_json=data.get("meta_json"),
    )
    db.session.add(lp)
    db.session.commit()
    return jsonify({"ok": True, "data": {"id": lp.id}}), 201
