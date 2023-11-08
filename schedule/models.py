from datetime import timedelta

from django.db import models

from users.models import User

NULLABLE = {
    'null': True,
    'blank': True
}


# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    related_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, **NULLABLE, verbose_name='Pleasant habit')

    place = models.CharField(max_length=100, verbose_name="Place", **NULLABLE)
    time_to_act = models.TimeField(verbose_name='Time', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='Action')
    is_pleasant = models.BooleanField(default=False, verbose_name='Is_pleasant', **NULLABLE)
    frequency = models.DurationField(default=timedelta(days=1), verbose_name='frequency')
    reward = models.CharField(max_length=100, verbose_name='Reward', **NULLABLE)
    time_to_complete = models.DurationField(default=timedelta(seconds=120), verbose_name='time_to_complete', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Is_public', **NULLABLE)


    def __str__(self):
        return f"{self.action} {self.time_to_act} {self.place}"

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
