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
    user_telegram_id = models.PositiveIntegerField(unique=True, verbose_name='user_id_telegram')
    user_telegram_name = models.CharField(max_length=100, unique=True, verbose_name='user_id_telegram', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

