# This module is made by https://github.com/SOME-1HING/
# You are free to use this module. But don't delete this commented text. Thank you.


import html

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleMessageHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, Filters

IMG_GM = "https://telegra.ph/file/fff37608fa21d9d3d0b39.jpg"
IMG_GN = "https://telegra.ph/file/1862c7260109e24ed4715.jpg"
IMG_HELLO = "https://telegra.ph/file/f3f2dc386a33e37f6cb05.png"
IMG_BYE = "https://telegra.ph/file/061054c8f73fe7ffbf6aa.mp4"

def goodnight(update: Update, context: CallbackContext):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        update.effective_message.reply_photo(
            IMG_GN,f"*Good Night:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
    except:
        reply = f"*Good Night:* {user1}"
        message.reply_text(reply)


def goodmorning(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        update.effective_message.reply_photo(
            IMG_GM,f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
    except:
        reply = f"*Good Morning:* {user1}"
        message.reply_text(reply)

def hello(update: Update, context: CallbackContext):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        update.effective_message.reply_photo(
            IMG_HELLO,f"*Hello* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
    except:
        reply = f"*Hello* {user1}"
        message.reply_text(reply)

def bye(update: Update, context: CallbackContext):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        update.effective_message.reply_animation(
            IMG_BYE, caption = f"*Bye!!* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
    except:
        reply = f"*Bye!!* {user1}"
        message.reply_text(reply)



GDMORNING_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(good morning|goodmorning)"), goodmorning, friendly="goodmorning", run_async = True
)
GDNIGHT_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(good night|goodnight)"), goodnight, friendly="goodnight", run_async = True
)
BYE_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(bye|brb|afk)"), bye, friendly="bye", run_async = True
)
HELLO_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(hello)"), hello, friendly="hello", run_async = True
)

dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)
dispatcher.add_handler(HELLO_HANDLER)
dispatcher.add_handler(BYE_HANDLER)

__handlers__ = [
    GDMORNING_HANDLER,
    GDNIGHT_HANDLER,
    HELLO_HANDLER,
    BYE_HANDLER
]