# Telegram Unsplash Bot

<!-- codex-repo-note:start -->
## Справка о репозитории / Repository note

**RU:** бот для тестовых и автоматизационных сценариев 2026 года.

**EN:** a bot for 2026 testing and automation scenarios.

**Статус / Status:** активный проект 2026 года; ожидает рефакторинга и переименования. / active 2026 project; refactoring and repository rename are pending.

**Текущее имя / Current name:** `testing_2026_bot`

**Плановое имя / Planned name:** `testing-2026-bot`

**Topics:** `automation`, `cleanup-pending`, `needs-rename`, `needs-review`, `python`, `status-active`, `testing`, `type-bot`
<!-- codex-repo-note:end -->


Простой Telegram-бот на Python, который отправляет случайные фотографии из Unsplash по запросу пользователя.

Бот предназначен для обучения и практики:
- работы с Telegram Bot API,
- подключения внешнего API (Unsplash),
- использования переменных окружения,
- развёртывания бота на хостинге (например, Render).

---

## Возможности бота

- Команда `/start` — приветствие и справка
- Команда `/ping` — проверка, что бот работает
- Команда `/photo <тема>` — отправка случайного фото из Unsplash по ключевому слову
- Корректная обработка ситуации, когда по запросу фото не найдено

---

## Требования

- Python **3.10+**
- Аккаунт в Telegram
- Аккаунт на Unsplash
- (опционально) GitHub для деплоя

---

## 1. Создание Telegram-бота

1. В Telegram открой **@BotFather**
2. Выполни команду:
```

/newbot

````
3. Задай имя и username бота
4. Скопируй выданный **BOT_TOKEN** — он понадобится позже

---

## 2. Получение Unsplash Access Key

1. Зарегистрируйся на https://unsplash.com
2. Перейди в раздел разработчиков:
https://unsplash.com/developers
3. Нажми **Register as a developer**
4. Создай новое приложение (**New Application**)
5. Заполни название и описание
6. После создания приложения скопируй поле:

**Access Key** ← это и есть `UNSPLASH_ACCESS_KEY`

⚠️ **Secret Key и Application ID для этого бота не нужны**

---

## 3. Клонирование проекта

```bash
git clone https://github.com/your-username/telegram-unsplash-bot.git
cd telegram-unsplash-bot
````

---

## 4. Установка зависимостей

Рекомендуется использовать виртуальное окружение:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

---

## 5. Настройка переменных окружения

В корне проекта создай файл **`.env`**:

```env
BOT_TOKEN=ваш_telegram_bot_token
UNSPLASH_ACCESS_KEY=ваш_unsplash_access_key
```

⚠️ Файл `.env` **не должен попадать в Git**
Он уже добавлен в `.gitignore`.

---

## 6. Запуск бота локально

```bash
python bot.py
```

Если всё настроено правильно, в консоли появится сообщение о запуске бота.

Открой Telegram и напиши боту:

```
/ping
/photo cat
```

---

## 7. Поведение бота

* Если по запросу есть фото → бот пришлёт изображение
* Если фото не найдено → бот предложит попробовать другой запрос
* Ошибки ключей проверяются при старте бота

---

## 8. Деплой на Render (кратко)

1. Залей проект в GitHub (без `.env`)
2. Зайди на [https://render.com](https://render.com)
3. Создай **Background Worker**
4. Подключи GitHub-репозиторий
5. Укажи:

   * **Build Command**:

     ```
     pip install -r requirements.txt
     ```
   * **Start Command**:

     ```
     python bot.py
     ```
6. В разделе **Environment Variables** добавь:

   * `BOT_TOKEN`
   * `UNSPLASH_ACCESS_KEY`
7. Запусти деплой

После этого бот будет работать 24/7.

---

## Структура проекта

```
.
├── bot.py              # основной код бота
├── config.py           # загрузка и проверка конфигурации
├── startup_checks.py   # проверки ключей при запуске
├── requirements.txt    # зависимости
├── .env                # переменные окружения (локально)
├── .gitignore
└── README.md
```

---

## Полезные замечания

* Unsplash лучше ищет по английским словам
* Demo-ключ Unsplash имеет лимиты (~50 запросов/час)
* Для продакшена рекомендуется добавить кэширование запросов

---

## Лицензия

Проект предназначен для учебных целей.
Фотографии предоставляются сервисом **Unsplash** с обязательным указанием авторства.

```

---

Если хочешь, следующим шагом могу:
- упростить README **под совсем “нулевого” пользователя**,
- добавить раздел **FAQ / типовые ошибки**,
- или адаптировать README **под отчёт / учебную работу**.
```
