import json
from pathlib import Path
from types import SimpleNamespace

with open(
    Path(__file__).resolve().parent.parent / "config.json",
    encoding="utf-8"
) as r:
    config = json.load(r, object_hook=lambda d: SimpleNamespace(**d))