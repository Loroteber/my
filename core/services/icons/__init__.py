import json
from pathlib import Path
from types import SimpleNamespace
from markupsafe import Markup
from ...logger import log

icons = {}

def build():
    log(__name__, "updating cache...")
    
    for icon in (Path('.').parent.parent / "res" / "static" / "icons").iterdir():
        if icon.is_file():
            log(__name__, icon.name)
            icons[icon.stem] = icon.read_text(encoding="utf-8")
        
    with open(Path(__file__).resolve().parent / "cache.json", "w", encoding="utf-8") as f:
        json.dump(icons, f, ensure_ascii=False)

    log(__name__, "updated successfully!", "succ")

def get():
    with open(
        Path(__file__).resolve().parent / "cache.json",
        encoding="utf-8"
    ) as r:
        data = json.load(r)

        return {
            key: Markup(value)
            for key, value in data.items()
        }