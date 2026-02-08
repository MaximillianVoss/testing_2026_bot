import re
import requests
import logging

logger = logging.getLogger("startup")


def check_telegram_token(token: str) -> None:
    """
    Базовая проверка формата BOT_TOKEN
    """
    if not token:
        raise RuntimeError("BOT_TOKEN is empty")

    # Простейшая проверка формата Telegram-токена
    if not re.match(r"^\d+:[A-Za-z0-9_-]{30,}$", token):
        raise RuntimeError("BOT_TOKEN has invalid format")

    logger.info("Telegram BOT_TOKEN format OK")


def check_unsplash_key(access_key: str) -> None:
    """
    Проверка, что Unsplash реально принимает ключ
    """
    if not access_key:
        raise RuntimeError("UNSPLASH_ACCESS_KEY is empty")

    url = "https://api.unsplash.com/photos/random"
    params = {"client_id": access_key}

    try:
        r = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        raise RuntimeError(f"Unsplash check failed: network error: {e}")

    if r.status_code == 401:
        raise RuntimeError(
            "Unsplash check failed: 401 Unauthorized "
            "(invalid or inactive Access Key)"
        )

    if r.status_code != 200:
        raise RuntimeError(
            f"Unsplash check failed: HTTP {r.status_code}: {r.text[:200]}"
        )

    logger.info("Unsplash ACCESS_KEY validated successfully")
