from rest_framework import serializers

from schedule.models import Habit
from schedule.validators import validate_related_fields_habits, validate_period, validate_time_to_complete, \
    validate_reward_fields_habits


class HabitSerializer(serializers.ModelSerializer):
    frequency = serializers.DurationField(validators=[validate_period])
    time_to_complete = serializers.DurationField(validators=[validate_time_to_complete])

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [validate_related_fields_habits, validate_reward_fields_habits]
