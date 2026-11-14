import json
from pathlib import Path
from types import SimpleNamespace
from .worker import start, run

def get():
    with open(
        Path(__file__).resolve().parent / "cache.json",
        encoding="utf-8"
    ) as r:
        return json.load(r, object_hook=lambda d: SimpleNamespace(**d))