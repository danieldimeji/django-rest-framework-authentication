from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SignUpSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name', 
            'username', 
            'email', 
            'password',
            'date_joined'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.email
        token['email'] = user.email
        return token
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
