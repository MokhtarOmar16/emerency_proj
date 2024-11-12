from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreatePasswordRetypeSerializer as BaseUserCreateSerializer
from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'phone_no', 'password',
                  'email', 'first_name', 'last_name']




class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'phone_no', 'email', 'first_name', 'last_name']