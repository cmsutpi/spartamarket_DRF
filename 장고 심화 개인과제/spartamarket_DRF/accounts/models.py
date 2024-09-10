from django.contrib.auth.models import AbstractUser
from django.db import models

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "")