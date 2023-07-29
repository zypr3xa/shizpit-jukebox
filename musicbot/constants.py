import os.path
import subprocess

try:
    VERSION = "2"
except Exception:
    VERSION = "version_unknown"

AUDIO_CACHE_PATH = os.path.join(os.getcwd(), "audio_cache")
DISCORD_MSG_CHAR_LIMIT = 2000
