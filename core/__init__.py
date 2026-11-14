from flask import Flask
from importlib import import_module
from pathlib import Path
from .config import config
from .services import music, icons, i18n
from . import errorpage

res_dir = Path(__file__).resolve().parent.parent / "res"

app = Flask(
    __name__,
    template_folder=res_dir / "templates",
    static_folder=res_dir / "static",
    static_url_path="/static"
)

errorpage.init(app)
i18n.init(app, res_dir)

for name, settings in vars(config.apps).items():
    if not settings.enabled:
        continue

    module = import_module(f"apps.{name}")

    app.register_blueprint(
        module.bp,
        url_prefix=settings.root
    )