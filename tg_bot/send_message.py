import requests


key = '6542951190:AAF1eAS-gmu5ICSjhO4frHnbwfDL5Jv5dD4'
# bot = telebot.TeleBot(key)

# bot.get_updates()
# bot.send_message(415965166, 'test')

updates = requests.get(f'https://api.telegram.org/bot{key}/getUpdates').json()
print(updates)
user_telegram_id = updates.get('result')[0].get('message').get('from').get('id')
print(user_telegram_id)

data = {
    'chat_id': user_telegram_id,
    'text': "habit.action"
}

test = requests.post(f'https://api.telegram.org/bot{key}/sendMessage', data)
