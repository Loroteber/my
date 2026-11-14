from . import bp, routes as r
from flask import render_template, request, send_from_directory
from core import res_dir
from core.services import music, icons, i18n
from pathlib import Path
import json

_socials = json.load(open(Path(__file__).resolve().parent / "socials.json", "r", encoding="utf-8"))
_devices = json.load(open(Path(__file__).resolve().parent / "devices.json", "r", encoding="utf-8"))
_banners = json.load(open(Path(__file__).resolve().parent / "banners.json", "r", encoding="utf-8"))
_icons = icons.get()

@bp.route(r.test)
def test():
    return "<h1>shit works fine</h1>"

@bp.route(r.main)
def main():
    return render_template("index.html", music=music.get(), icons=_icons, socials=_socials, banners=_banners, lang=i18n.getLocale())

@bp.route(r.devices)
def devices():
    return render_template("devices.html", icons=_icons, title="Devices", devices=_devices)

# love this shit
@bp.route(r.icon)
def icon():
    return send_from_directory(res_dir / "static/img", "favicon.ico")