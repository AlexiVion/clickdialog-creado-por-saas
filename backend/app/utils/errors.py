from flask import jsonify

def api_error(code: str, message: str, status: int = 400, details=None):
    return jsonify({
        "ok": False,
        "error": {
            "code": code,
            "message": message,
            "details": details or {}
        }
    }), status
