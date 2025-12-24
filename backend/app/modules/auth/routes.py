from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from datetime import datetime, timedelta

from app.extensions import db
from app.utils.errors import api_error
from .models import User, Tenant, Role, UserRole

bp = Blueprint("auth", __name__, url_prefix="/api/auth")

def _jwt_encode(payload: dict) -> str:
    secret = current_app.config["JWT_SECRET"]
    return jwt.encode(payload, secret, algorithm="HS256")

def _jwt_decode(token: str) -> dict:
    secret = current_app.config["JWT_SECRET"]
    return jwt.decode(token, secret, algorithms=["HS256"])

@bp.post("/seed")
def seed_dev():
    """Seed mínimo para dev (solo si DB vacía)."""
    if User.query.first():
        return jsonify({"ok": True, "data": {"seeded": False}})

    tenant = Tenant(name="Default Tenant")
    db.session.add(tenant)
    db.session.commit()

    # roles
    role_names = ["superadmin", "admin", "client"]
    roles = []
    for rn in role_names:
        r = Role(name=rn)
        db.session.add(r)
        roles.append(r)
    db.session.commit()

    # user admin
    u = User(tenant_id=tenant.id, email="admin@local", password_hash=generate_password_hash("admin"))
    db.session.add(u)
    db.session.commit()

    # assign superadmin
    superadmin = Role.query.filter_by(name="superadmin").first()
    if superadmin:
        db.session.add(UserRole(user_id=u.id, role_id=superadmin.id))
        db.session.commit()

    return jsonify({"ok": True, "data": {"seeded": True, "email": u.email, "password": "admin"}})

@bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    if not email or not password:
        return api_error("VALIDATION_ERROR", "Faltan email o password", 400)

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return api_error("AUTH_INVALID_CREDENTIALS", "Credenciales inválidas", 401)

    exp = datetime.utcnow() + timedelta(hours=24)
    token = _jwt_encode({
        "sub": str(user.id),
        "tenant_id": user.tenant_id,
        "exp": int(exp.timestamp()),
    })
    return jsonify({"ok": True, "data": {"token": token}})

@bp.get("/me")
def me():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return api_error("AUTH_REQUIRED", "Falta Bearer token", 401)

    token = auth.split(" ", 1)[1].strip()
    try:
        payload = _jwt_decode(token)
    except Exception:
        return api_error("AUTH_REQUIRED", "Token inválido", 401)

    user = User.query.get(int(payload["sub"]))
    if not user:
        return api_error("NOT_FOUND", "Usuario no encontrado", 404)

    return jsonify({"ok": True, "data": {"id": user.id, "email": user.email, "tenant_id": user.tenant_id}})
