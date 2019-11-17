# Scott Ng 2019
# University of Southern California (USC)

# Shibas every hour!
# Telegram bot using the python-telegram-bot wrapper

import telegram
from telegram.ext import (Updater, CommandHandler, Filters)
from apscheduler.schedulers.background import BackgroundScheduler
from config import *
from flickr import *


sendTimeInterval = sendTimeIntervals[0]

# Scheduler to send pictures
scheduler = BackgroundScheduler()

# Get updater and dispatcher from telegram
updater = Updater(BOT_TOKEN, use_context = True)
dispatcher = updater.dispatcher

# Enable logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# used for testing the logic of the bot
def get_rand_photo_url():
    return "https://upload.wikimedia.org/wikipedia/commons/6/6b/Taka_Shiba.jpg"

# Start command: send an introduction message
def command_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="I will send you shibas on demand! Start with typing /shiba, or type /help for a list of commands!")
    
    # scheduler.add_job(send_shiba, 
    #     'interval', 
    #     seconds=5, 
    #     args=[update, context], 
    #     id=str(update.effective_chat.id))
    # scheduler.start()

# Shiba command: send an image of a shiba
def command_shiba(update, context):
	send_shiba(update, context)

# Help command: send a list of all commands
def command_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="/shiba: return an image")

# Interval command: set interval
def command_set_interval(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="How often would you like to receive images?")

    # after being called, bring up an inline keyboard menu! with the options 
    custom_keyboard = [['10 s', '1 min', '30 min'], 
                   ['1 hr', '3 hr', '24 hr']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                 text="Choose an interval.", 
                 reply_markup=reply_markup)

    # get response

    # set interval by changing scheduler

# Stop command:
def command_stop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Goodbye!")
    

def send_shiba(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, 
        photo=get_rand_photo_url())
    
def main():
    commands = { 
        "start":command_start,
        "shiba":command_shiba,
        "help":command_help,
        "setinterval":command_set_interval
    }

    for name, function in commands.items():
        updater.dispatcher.add_handler(CommandHandler(name, function))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


# Get an image from queue (Firebase)

# Add an image to queue via URL (Firebase)
# Store image under USERID


# how would you set custom intervals for each user?
# get userID/chatID/channelID
# store locally or in database as a hashmap (uID, interval)
# define intervals as 1 min, 1 hr, 