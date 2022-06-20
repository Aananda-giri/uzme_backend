from wsgiref import validate
from django.contrib.auth.models import User
# from more_itertools import first
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        data= {'username':username, 'first_name':first_name, 'last_name':last_name, 'email':email, 'password':password}
        
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create_user(data)

        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]