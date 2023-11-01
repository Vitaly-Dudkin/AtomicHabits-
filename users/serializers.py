from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    tg_bot_address = serializers.SerializerMethodField()

    def get_tg_bot_address(self):
        return 'you can find your id here https://t.me/my_id_bot'

    class Meta:
        model = User
        fields = '__all__'
