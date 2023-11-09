from rest_framework.exceptions import ValidationError


def validate_related_fields_habits(value):
    if value.get('reward') and value.get('is_pleasant'):
        raise ValidationError('Pleasant habit cant has a reward')
    if value.get('related_habit') and value.get('is_pleasant'):
        raise ValidationError('Pleasant habit cant has a related habit')


def validate_reward_fields_habits(value):
    if sum([bool(value.get('related_habit')), bool(value.get('reward')), bool(value.get('is_pleasant'))]) < 1:
        raise ValidationError('You need to choose the reward or related_habit for the unpleasant habit')


def validate_period(value):
    if value.days >= 8:
        raise ValidationError('Period should be less then 7')


def validate_time_to_complete(value):
    if value.total_seconds() > 120:
        raise ValidationError('Time to complete a habit has to be less then 120 seconds')
