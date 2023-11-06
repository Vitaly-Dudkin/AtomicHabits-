from datetime import datetime
import os
import dotenv
import requests
from celery import shared_task

from schedule.models import Habit

dotenv.load_dotenv()


@shared_task
def check_time_habits():
    datetime_now = datetime.now()
    time_now = datetime_now.strftime("%H:%M:00")
    habits = Habit.objects.filter(time_to_act=time_now)
    for habit in habits:
        data = {
            'chat_id': 415965166,
            'text': f"Hello {habit.user.email}"
        }

        requests.post(f"https://api.telegram.org/bot{os.getenv('TG_ACCESS_TOKEN')}/sendMessage", data)



# import requests
#
# key = '6542951190:AAF1eAS-gmu5ICSjhO4frHnbwfDL5Jv5dD4'
# # bot = telebot.TeleBot(key)
#
# # bot.get_updates()
# # bot.send_message(415965166, 'test')
#
# updates = requests.get(f'https://api.telegram.org/bot{key}/getUpdates').json()
#
# point = 1
#
# data = {
#     'chat_id': 415965166,
#     'text': "habi"
# }
#
# test = requests.post(f'https://api.telegram.org/bot{key}/sendMessage', data)
