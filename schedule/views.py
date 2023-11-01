from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from schedule.models import Habit
from schedule.paginators import HabitPaginator
from schedule.permissions import IsOwner, IsSuperuser
from schedule.serializers import HabitSerializer


# Create your views here.


class HabitCreateListView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
            Getting Lesson Objects based on User
        """
        queryset = super().get_queryset()
        print(Habit.objects.filter(is_public=True))

        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset.all()
        elif self.request.user:
            return queryset.filter(user=self.request.user)
        else:
            return queryset.none()

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsSuperuser]


class PublicHabitsListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]

