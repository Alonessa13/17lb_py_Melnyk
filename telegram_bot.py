import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from assistant import Assistant

API_TOKEN = '7447782736:AAG2RCTOqR9Apq-eVkWJFPCc2rmYUJk2Oao'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
assistant = Assistant()

user_states = {}

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привіт! Я твій нотатник.\nКоманди: /add, /list, /search, /help")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("/add — додати нотатку\n/list — список нотаток\n/search — пошук нотаток")

@dp.message(Command("list"))
async def cmd_list(message: Message):
    notes = assistant.list_notes()
    if notes:
        await message.answer("\n".join(f"{i+1}. {n}" for i, n in enumerate(notes)))
    else:
        await message.answer("Список нотаток порожній.")

@dp.message(Command("add"))
async def cmd_add(message: Message):
    user_states[message.from_user.id] = 'awaiting_note'
    await message.answer("Введіть текст нотатки:")

@dp.message(Command("search"))
async def cmd_search(message: Message):
    user_states[message.from_user.id] = 'awaiting_search'
    await message.answer("Введіть ключове слово для пошуку:")

@dp.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    state = user_states.get(user_id)

    if state == 'awaiting_note':
        assistant.add_note(message.text)
        await message.answer("Нотатку додано.")
        user_states.pop(user_id)
    elif state == 'awaiting_search':
        results = assistant.search_notes(message.text)
        if results:
            await message.answer("\n".join(f"- {n}" for n in results))
        else:
            await message.answer("Нічого не знайдено.")
        user_states.pop(user_id)
    else:
        await message.answer("Невідома команда. Напишіть /help")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
