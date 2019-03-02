# authentication
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class AccountListAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #permission_classes = (IsAdminUser,)

class AccountUpdateView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailsView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDeleteView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Registration
class UserRegistrationView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer