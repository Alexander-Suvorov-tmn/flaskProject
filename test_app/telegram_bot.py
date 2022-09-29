from dotenv import dotenv_values
from datetime import datetime
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from test_app import sess, OrderData

conf = dotenv_values(".env")
API_TOKEN = conf.get('TG_ID')
bot = Bot(token=API_TOKEN)
updater = Updater(token=API_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет!")


def callback_request(context):
    global order_count
    data = sess.query(OrderData).all()
    day = datetime.now()
    for i in data:
        if day > i.delivery_time:
            context.bot.send_message(chat_id=context.job.context, text=f'срок поставки по записи № {i.id} прошел')



def callback_timer(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Начинаем!')
    updater.job_queue.run_repeating(callback_request, 5, context=update.message.chat_id)


start_handler = CommandHandler('start', start)

dispatcher.add_handler(CommandHandler('start', callback_timer))
dispatcher.add_handler(start_handler)
