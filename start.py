from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from keyboards import start_kb, again_kb
from services import send_photo, write_in_file
from bot import bot, dispatcher
from aiogram.types import FSInputFile


class FSMFillForm(StatesGroup):
    fill_question = State()


@dispatcher.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text='Хочешь написать свой вопрос в чат или просто его задумать?',
                         reply_markup=start_kb)


@dispatcher.callback_query(lambda c: c.data == 'get_photo_with_question')
async def process_get_photo_with_question(callback, state):
    await bot.send_message(callback.message.chat.id, 'Напиши и отправь свой вопрос')
    await callback.message.delete()
    await state.set_state(FSMFillForm.fill_question)


@dispatcher.callback_query(lambda c: c.data == 'get_photo_now')
async def process_get_photo_now(callback):
    await bot.send_photo(callback.from_user.id, FSInputFile(send_photo(callback)))
    await bot.send_message(callback.from_user.id, text='Хочешь задать ещё один вопрос?', reply_markup=again_kb)
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
    await callback.message.delete()


@dispatcher.message(FSMFillForm.fill_question)
async def process_fill_question(message, state):
    write_in_file(message)
    await state.clear()
    await bot.send_photo(message.from_user.id, FSInputFile(send_photo(message)))
    await message.answer(text='Хочешь задать ещё один вопрос?', reply_markup=again_kb)


if __name__ == '__main__':
    dispatcher.run_polling(bot, skip_updates=False)
