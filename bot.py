import logging
import requests

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN, UNSPLASH_ACCESS_KEY  # <-- берём конфиг отсюда
from startup_checks import check_telegram_token, check_unsplash_key
from config import BOT_TOKEN, UNSPLASH_ACCESS_KEY

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("bot")


def unsplash_random_photo(query: str | None = None) -> dict:
    url = "https://api.unsplash.com/photos/random"

    params = {
        "orientation": "portrait",
        "client_id": UNSPLASH_ACCESS_KEY,
    }

    if query:
        q = query.strip()
        if q:
            params["query"] = q

    r = requests.get(url, params=params, timeout=15)

    # Unsplash: 404 = "No photos found"
    if r.status_code == 404:
        raise LookupError("NO_PHOTOS_FOUND")

    r.raise_for_status()
    data = r.json()

    return {
        "image_url": data["urls"]["regular"],
        "author_name": data["user"]["name"],
        "author_profile": data["user"]["links"]["html"],
        "photo_page": data["links"]["html"],
    }



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я бот с фото из Unsplash.\n"
        "Команды:\n"
        "/photo <тема> — случайное фото по теме\n"
        "/ping — проверка, что бот жив"
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("pong ✅")


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = " ".join(context.args).strip() if context.args else None

    try:
        p = unsplash_random_photo(query=query)

    except LookupError:
        await update.message.reply_text(
            "По этому запросу ничего не нашлось 😅\n"
            "Попробуй другое слово (лучше по-английски), например:\n"
            "/photo cat"
        )
        return

    except requests.HTTPError as e:
        logger.exception("Unsplash HTTP error")
        await update.message.reply_text(
            f"Unsplash вернул ошибку: {e}\n"
            "Проверь ключ и лимиты."
        )
        return

    except Exception:
        logger.exception("Unexpected error")
        await update.message.reply_text("Неожиданная ошибка при получении фото.")
        return

    caption = (
        f"📸 *Photo* {('по теме: ' + query) if query else ''}\n"
        f"Автор: [{p['author_name']}]({p['author_profile']})\n"
        f"[Открыть на Unsplash]({p['photo_page']})"
    )

    await update.message.reply_photo(
        photo=p["image_url"],
        caption=caption,
        parse_mode=ParseMode.MARKDOWN,
    )



def main() -> None:
    # === Startup checks ===
    check_telegram_token(BOT_TOKEN)
    check_unsplash_key(UNSPLASH_ACCESS_KEY)

    logger.info("All startup checks passed, starting bot")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("photo", photo))

    app.run_polling(close_loop=False)


if __name__ == "__main__":
    main()
