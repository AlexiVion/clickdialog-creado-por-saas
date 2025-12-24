# Infra / Deploy (estándar)

Este folder contiene snippets y guías para deploy repetible.

## Recomendación (tu regla): **no editar en producción**
- Todo cambio se hace local.
- El server solo recibe deploy desde Git (`git pull`) + restart systemd.

## Pasos típicos (server)
1) Clonar repo del SaaS
2) Crear venv + instalar requirements
3) Instalar service systemd
4) Configurar Caddy
5) Deploy con `deploy.sh` (pull + migrate + restart)
