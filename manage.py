from core.services import icons
import sys

if sys.argv[1] == "icons":
    if sys.argv[2] == "build":
        icons.build()