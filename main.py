import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

dp = Dispatcher()

@dp.message(Command("start"))
async def on_start(m: Message):
    chat_id = m.chat.id
    thread_id = m.message_thread_id
    text = (
        "✅ Бот запущен.\n"
        f"chat_id: {chat_id}\n"
        f"thread_id: {thread_id}"
    )
    print(text)
    await m.reply(text)

@dp.message(Command("ids", "where"))
async def send_ids(m: Message):
    chat_id = m.chat.id
    thread_id = m.message_thread_id
    text = (
        "ℹ️ Текущие идентификаторы:\n"
        f"chat_id: {chat_id}\n"
        f"thread_id: {thread_id}"
    )
    print(text)
    await m.reply(text)

@dp.message(F.forum_topic_created)
async def on_topic_created(m: Message):
    thread_id = m.message_thread_id
    name = m.forum_topic_created.name if m.forum_topic_created else "<без имени>"
    text = f"🧵 Топик создан: {name}\nthread_id: {thread_id}"
    print(text)
    await m.answer(text)

@dp.message()
async def log_any(m: Message):
    chat_id = m.chat.id
    thread_id = m.message_thread_id
    who = m.from_user.full_name if m.from_user else "unknown"
    payload = m.text or m.caption or "<non-text>"
    logging.info(
        f"[MSG] from={who!r} chat_id={chat_id} thread_id={thread_id} payload={payload!r}"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(BOT_TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
