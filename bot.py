import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.filters import Command

API_TOKEN = "8807668932:AAHH2oLhOaFXe3MXjCnjOgS9GhOZKtNjRqA"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def starting_bot(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть игру", web_app=WebAppInfo(url="https://ghut-coinn-production.up.railway.app/"))]
    ])
    await message.answer("👋 Йо, ты попал в Ghut Coin — место, где палец становится богатым 💰\n\n🔥 Это не просто бот — это настоящая тапалка на максимум, где каждый клик превращается в монеты. Здесь нет сложных правил — только ты, экран и бесконечный фарм.\n\nВ конце сезона планируется листинг Ghut Coin 🚀\nВсе натапанные монеты будут конвертированы — и ты сможешь обменять их на реальные деньги 💸\n⚠️ Чем больше нафармишь сейчас — тем сильнее будет твой результат потом.", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
