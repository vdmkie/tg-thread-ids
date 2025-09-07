import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Установи переменную окружения BOT_TOKEN.")

dp = Dispatcher()

@dp.message(Command("where", "ids"))
async def send_ids(m: Message):
    chat_id = m.chat.id
    thread_id = m.message_thread_id
    chat_type = m.chat.type
    text = (
        "📌 Информация о месте:\n"
        f"▫️ chat_id: {chat_id}\n"
        f"▫️ thread_id: {thread_id}\n"
        f"▫️ chat_type: {chat_type}"
    )
    print(text)
    await m.reply(text)

# Логируем все сообщения
@dp.message()
async def log_any(m: Message):
    logging.info(
        f"[MSG] chat_id={m.chat.id}, thread_id={m.message_thread_id}, text={m.text}"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(BOT_TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
