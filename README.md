# ClickDialog (generado por Umbrella Core)

Registry + Analytics + Dashboard multi-tenant

## Módulos habilitados
auth, landingpages, chatbot, analytics, integration

## Estructura
- `backend/` Flask API
- `frontend/` Astro (static)
- `infra/` deploy estándar (Caddy + systemd)
- `docs/` documentación generada

## Dev quickstart

### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# Migraciones + seed
flask db upgrade
curl -X POST http://localhost:5005/api/auth/seed

flask run --port 5005
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Contratos
Este SaaS respeta los contratos de Umbrella Core:
- `/api/health`
- Errores `{ ok:false, error:{code,message,details} }`
