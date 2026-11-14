from . import bp, routes as r
from flask import render_template
from core.services import music, icons
from pathlib import Path
import json

_icons = icons.get()

@bp.route(r.main)
def main():
    return "чювак зачем ты сюда полез ну ок"

@bp.route(r.music)
def devices():
    return render_template("music.html", music=music.get(), icons=_icons)