from django.urls import path

from schedule.apps import ScheduleConfig
from schedule.views import HabitRetrieveUpdateDestroyAPIView, PublicHabitsListView, HabitCreateListView

app_name = ScheduleConfig.name

urlpatterns = [
    path('', HabitCreateListView.as_view(), name='list-create'),
    path('<int:pk>/', HabitRetrieveUpdateDestroyAPIView.as_view(), name='habits'),

    path('public_habits/', PublicHabitsListView.as_view(), name='public_habits')
]
