from flask import Blueprint
from core.routes import routes

bp = Blueprint(
    __name__.split(".")[-1],
    __name__
    )
    
routes = routes(__file__)

from . import app