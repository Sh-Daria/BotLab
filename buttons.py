from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

main_kb = [
    [KeyboardButton(text='Открыть список групп')],
    [KeyboardButton(text='Выбор группы')]
    ]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True)

report = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text='Отчёт', callback_data = 'report')]
    ])