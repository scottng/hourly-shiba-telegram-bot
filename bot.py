# Scott Ng 2019
# University of Southern California (USC)

# Shibas every hour!
# Telegram bot using the python-telegram-bot wrapper

import config
import telegram
import logging
from telegram.ext import (Updater, CommandHandler, Filters)

'''
    Features I want to add:
    - Custom time intervals for each user/group/channel
    - Get link to source
'''

# Enable logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Get an image from flickr
def getRandPhotoURL():
    return "https://upload.wikimedia.org/wikipedia/commons/6/6b/Taka_Shiba.jpg"

# Start command: send an introduction message
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I will send you shibas on demand! Start with typing /shiba, or type /help for a list of commands!")

# Shiba command: send an image of a shiba (calls getRandPhotoURL()) 
def shiba(update, context):
	context.bot.send_photo(chat_id=update.effective_chat.id, photo=getRandPhotoURL())

# Help command: send a list of all commands
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/shiba: return an image")

def main():
    # Get updater and dispatcher
    updater = Updater(BOT_TOKEN, use_context = True)
    dispatcher = updater.dispatcher

    # set handlers for commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('shiba', shiba))
    dispatcher.add_handler(CommandHandler('help', help))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()