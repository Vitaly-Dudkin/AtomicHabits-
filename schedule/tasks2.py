import os

import dotenv
import requests
dotenv.load_dotenv()

data = {
    'chat_id': 415965166,
    'text': f"test "
}

requests.post(f"https://api.telegram.org/bot{os.getenv('TG_ACCESS_TOKEN')}/sendMessage", data)