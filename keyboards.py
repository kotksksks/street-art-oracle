from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Хочу написать вопрос', callback_data='get_photo_with_question')],
        [InlineKeyboardButton(text='Лучше оставлю только в голове', callback_data='get_photo_now')]]
)

start_kb = keyboard

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да, напишу', callback_data='get_photo_with_question'),
         InlineKeyboardButton(text='Задам про себя', callback_data='get_photo_now')]]
)

again_kb = keyboard
