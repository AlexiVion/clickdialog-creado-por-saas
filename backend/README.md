# ClickDialog — Backend (Flask)

## Requisitos
- Python 3.11+

## Setup (dev)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt

# Variables
cp .env.example .env

# DB (SQLite por defecto)
flask db upgrade

# Run
flask run --port 5005
```

## Health
- `GET /api/health`

## Auth
- `POST /api/auth/login`
- `GET /api/auth/me`
