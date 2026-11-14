import json
from pathlib import Path
from types import SimpleNamespace

def routes(path):
    with open(
        Path(path).resolve().parent / "routes.json",
        encoding="utf-8"
    ) as r:
        return json.load(r, object_hook=lambda d: SimpleNamespace(**d))