from . import bp, routes as r
from flask import render_template


@bp.route(r.test)
def test():
    return "<h1>shit works fine</h1>"

@bp.route(r.main)
def main():
    return render_template("index.html")