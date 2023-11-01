from django.contrib import admin

from schedule.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('reward', 'is_pleasant', 'related_habit', 'user', 'time_to_complete')
