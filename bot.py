# Scott Ng 2019
# University of Southern California (USC)

# Shibas every hour!
# Telegram bot using the python-telegram-bot wrapper

import os
import telegram
from telegram.ext import (Updater, CommandHandler, Filters)
from flickr import *

# Get config variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_NAME = os.environ.get('CHANNEL_NAME')
WEBHOOK = os.environ.get('WEBHOOK')

# Enable logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def callback_send_to_channel(context: telegram.ext.CallbackContext):
    photo = get_photo()

    context.bot.send_photo(chat_id=CHANNEL_NAME, 
        photo=photo[0],
        caption="Source: " + photo[1])

# Start command: send an introduction message
def command_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="I will send you shibas on demand! Start with typing /shiba, or type /help for a list of commands!")

# Shiba command: send an image of a shiba
def command_shiba(update, context):
    photo = get_photo()

    context.bot.send_photo(chat_id=update.effective_chat.id, 
        photo=photo[0],
        caption="Source: " + photo[1])

# Help command: send a list of all commands
def command_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="/shiba: return an image")

# Stop command:
def command_stop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Goodbye!")
    
def main():

    # Get updater and dispatcher from telegram
    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(BOT_TOKEN)

    # Set up webhook
    updater.start_webhook(listen='0.0.0.0',
                      port=PORT,
                      url_path=BOT_TOKEN)

    # Get dispatcher from updater
    dispatcher = updater.dispatcher

    # Get job queue from updater
    job_queue = updater.job_queue

    # Add repeating job to send shibas
    job_seconds = job_queue.run_repeating(callback_send_to_channel,
        interval = 3600,
        first = 0)

    commands = { 
        "start":command_start,
        "shiba":command_shiba,
        "help":command_help,
    }

    for name, function in commands.items():
        updater.dispatcher.add_handler(CommandHandler(name, function))

    # Start listening for updates through the webhook
    updater.bot.set_webhook(WEBHOOK)
    updater.idle()

if __name__ == '__main__':
    main()