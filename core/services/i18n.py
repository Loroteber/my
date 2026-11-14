from flask import request
from flask_babel import Babel
from ..logger import log

def getLocale():
    language = request.args.get('l')

    if language in ['ru', 'en']:
        return language

    return request.accept_languages.best_match(['ru', 'en']) or 'en'

def init(app, res_dir):
    log(__name__, "initialising i18n...")
    
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = str(res_dir / "locales")
    app.config['BABEL_DEFAULT_LOCALE'] = "en"

    babel = Babel(app, locale_selector=getLocale)
    babel.init_app(app, locale_selector=getLocale)