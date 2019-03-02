from django.contrib.auth.models import User
from rest_framework import serializers
from django import forms
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(
          write_only=True,
          style={'input_type': 'password', 'placeholder': 'Password'},
    )
    class Meta:
       model = User
       fields = ('password', 'username', 'first_name', 'last_name',)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        if 'password' in validated_data:
              user.set_password(validated_data['password'])
              user.save()
        return user