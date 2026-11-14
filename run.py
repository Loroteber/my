import os
from core import app, music, icons

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        icons.build()
        music.start()

    app.run(debug=True)