from rest_framework import serializers

from schedule.models import Habit
from schedule.validators import validate_related_fields_habits, validate_period, validate_time_to_complete, \
    validate_reward_fields_habits


class HabitSerializer(serializers.ModelSerializer):
    period = serializers.DurationField(validators=[validate_period])
    time_to_complete = serializers.DurationField(validators=[validate_time_to_complete])
    related_habit = serializers.SerializerMethodField()

    def get_related_habit(self, instance):
        if instance.related_habit:
            return f'{instance.related_habit}'

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [validate_related_fields_habits, validate_reward_fields_habits]
