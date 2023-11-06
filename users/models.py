from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    user_telegram_id = models.PositiveIntegerField(unique=True, verbose_name='user_id_telegram', **NULLABLE)
    user_telegram_name = models.CharField(max_length=100, unique=True, verbose_name='user_id_telegram', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

# curl -s -X POST $URL -d caht_id=$CHAT_ID -d text='#MESSAGE'
# https://api.telegram.org/bot6542951190:AAF1eAS-gmu5ICSjhO4frHnbwfDL5Jv5dD4/sendMessage

