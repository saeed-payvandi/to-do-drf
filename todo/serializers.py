from rest_framework import serializers
from .models import ToDo, User
# from django.contrib.auth import get_user_model

# User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
        # fields = ['id', 'title', 'content']


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(read_only=True, many=True)

    class Meta():
        model = User
        fields = '__all__'


# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField
#     title = serializers.CharField
