import importlib
from flask import Flask
from .config import Config

def load_modules(app: Flask):
    cfg = Config()
    enabled = cfg.MODULES_ENABLED

    # Importa cada módulo instalado en app/modules/<name>/module.py
    for slug in enabled:
        mod_path = f"app.modules.{slug}.module"
        module = importlib.import_module(mod_path)
        if hasattr(module, "register"):
            module.register(app)
