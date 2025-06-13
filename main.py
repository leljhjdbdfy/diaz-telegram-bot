
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import logging
import os

API_TOKEN = os.getenv("API_TOKEN")

# Включаем логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- Главное меню ---
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add("📅 Записаться", "💅 Услуги")
main_kb.add("👩‍🎨 Мастера", "📸 Работы")
main_kb.add("📍 Адрес", "📞 Контакты")

# --- Команды ---
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я бот салона красоты Diaz 💅\n\nВыбери, что тебе нужно:",
        reply_markup=main_kb
    )

@dp.message_handler(lambda message: message.text == "📅 Записаться")
async def handle_booking(message: types.Message):
    btn = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Перейти к записи на DIkidi", url="https://dikidi.ru/ru/profile/diaz_viz_1648663")
    )
    await message.answer("Запись открыта 24/7. Нажми кнопку ниже:", reply_markup=btn)

@dp.message_handler(lambda message: message.text == "💅 Услуги")
async def handle_services(message: types.Message):
    text = "💅 Наши услуги:\n\n"
    text += "• Маникюр — от 1800₽\n"
    text += "• Педикюр — от 2500₽\n"
    text += "• Наращивание\n"
    text += "• Архитектура бровей\n"
    text += "• Ламинирование и окрашивание ресниц"
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "👩‍🎨 Мастера")
async def handle_masters(message: types.Message):
    text = "👩‍🎨 Наши мастера:\n\n"
    text += "• Дарья — маникюр, педикюр\n"
    text += "• Ксения — маникюр, педикюр\n"
    text += "• Виктория — маникюр, педикюр\n"
    text += "• Юлия — брови и ресницы"
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "📍 Адрес")
async def handle_address(message: types.Message):
    await message.answer("📍 Екатеринбург, ул. Начдива Васильева, 34\nОриентир: рядом с [уточнить ориентир]\n🕙 Ежедневно с 10:00 до 20:00")

@dp.message_handler(lambda message: message.text == "📸 Работы")
async def handle_works(message: types.Message):
    await message.answer("📸 Примеры наших работ ты можешь посмотреть в Instagram: @diaz_nail_ekb")

@dp.message_handler(lambda message: message.text == "📞 Контакты")
async def handle_contacts(message: types.Message):
    await message.answer("📞 WhatsApp: +7 (932) 122-33-99\n📸 Instagram: @diaz_nail_ekb")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
