from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler


def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Привет',
    )


def main():
    print('Start')

    updater = Updater(
        token='1083922392:AAEWHCeacExBsFQwyitmqqDmGu3Y2sdlq1o',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
