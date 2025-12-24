# Arquitectura — ClickDialog

## Módulos habilitados
auth, landingpages, chatbot, analytics, integration

## Dependencias (simple)
```mermaid
graph TD
  auth[auth]
  landing[landingpages]
  chatbot[chatbot]
  analytics[analytics]
  integration[integration]

  landing --> auth
  chatbot --> auth
  analytics --> auth
  integration --> landing
  integration --> chatbot
```
