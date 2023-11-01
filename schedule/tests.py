from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from schedule.models import Habit
from users.models import User


# Create your tests here.


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='dudkin231@mail.ru',
            user_telegram_id=415965166,
            user_telegram_name='Vital0077'
        )

        self.habit = Habit.objects.create(
            user=self.user,
            related_habit=None,
            place='home',
            time_to_act='00:02:00',
            action='take a cold shower',
            is_pleasant=False,
            time_to_complete='00:00:10',
            period='1 00:00:00',
        )

        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        response = self.client.get(
            reverse('schedule:list-create')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [
                {
                    "id": self.habit.pk,
                    "user": self.user.id,
                    "related_habit": self.habit.related_habit,
                    "place": self.habit.place,
                    'time_to_act': self.habit.time_to_act,
                    "action": self.habit.action,
                    "is_pleasant": self.habit.is_pleasant,
                    "period": self.habit.period,
                    "reward": self.habit.reward,
                    "time_to_complete": self.habit.time_to_complete,
                    "is_public": self.habit.is_public

                }
            ]
        )

    def test_create_habit(self):
        data = {
            "id": self.habit.pk,
            "user": self.user.id,
            "time_to_act": '00:02:00',
            "action": 'take a cold shower',
            "is_pleasant": False,
            "reward": 'another cold shower',
            "time_to_complete": "00:02:00",
            "period": '1 00:00:00',
        }

        response = self.client.post(
            reverse("schedule:list-create"),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_delete_habit(self):
        response = self.client.delete(
            reverse('schedule:habits', args=[self.habit.pk]),
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_update_habit(self):
        update_data = {
            "id": self.habit.pk,
            "user": self.user.id,
            "time_to_act": '00:02:00',
            "action": 'take a very cold shower',
            "is_pleasant": False,
            "reward": 'another cold shower',
            "time_to_complete": "00:02:00",
            "period": '1 00:00:00',
        }

        response = self.client.put(
            reverse("schedule:habits", args=[self.habit.pk]),
            data=update_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_habit(self):
        response = self.client.get(
            reverse('schedule:habits', args=[self.habit.pk])
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)
