import time
import requests
import json
import threading
from pathlib import Path
from ...config import config
from ...logger import log

_running = False
_lock = threading.Lock()

session = requests.Session()

session.proxies.update({
    "http": "socks5h://127.0.0.1:2080",
    "https": "socks5h://127.0.0.1:2080"
})

log(__name__, "starting worker...")

def run():
    while True:
        log(__name__, "updating cache...")
        try:
            r = session.get(
                'https://ws.audioscrobbler.com/2.0/',
                params={
                    'method': 'user.getRecentTracks',
                    'user': 'loroteber',
                    'api_key': config.music.token,
                    'format': 'json',
                    'limit': 1
                },
                timeout=10
            )
            r.raise_for_status()

            data = r.json()

            if "error" not in data:
                with open(Path(__file__).resolve().parent  / "cache.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False)
                log(__name__, f"updated successfully! next update in {config.music.upd_rate}s...", "succ")
            else:
                raise ValueError(data)
        except Exception as e:
            log(__name__, f"error while updating: {e}\n\nRetrying in {config.music.upd_rate}s...")

        time.sleep(int(config.music.upd_rate))

def start():
    global _running

    with _lock:
        if _running:
            return

        _running = True

    threading.Thread(
        target=run,
        daemon=True
    ).start()