import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

def env_required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required config value: {name} (env file: {ENV_PATH})")
    return value

BOT_TOKEN = env_required("BOT_TOKEN")
UNSPLASH_ACCESS_KEY = env_required("UNSPLASH_ACCESS_KEY")
