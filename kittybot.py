import logging
import os

import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

from dotenv import load_dotenv 

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    """Get random picture from from API."""
    try:
        response = requests.get(URL)
    except Exception as error:
        # Печатать информацию в консоль теперь не нужно:
        # всё необходимое будет в логах
        # print(error)
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    """Send random picture to the chat."""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def wake_up(update, context):
    """Send a message to the new user, makes button."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри какого котика я тебе нашел'.format(name),
        reply_markup=button
    )

    context.bot.send_photo(chat.id, get_new_image())


def main():
    """Execute bot commands."""
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
