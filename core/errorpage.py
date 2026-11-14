from flask import render_template
from .services import icons
from werkzeug.exceptions import HTTPException

_icons = icons.get()

def init(app):
    @app.errorhandler(HTTPException)
    def handle_error(error):
        return render_template(
            'error.html',
            code=error.code,
            name=error.name,
            description=error.description,
            icons = _icons
        ), error.code