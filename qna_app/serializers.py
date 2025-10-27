from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group


class AudienceRegistrationSerializer(serializers.Serializer):
    """
    Serializer for audience member registration (passwordless)
    Only requires a unique nickname that maps to the User.username field
    """
    nickname = serializers.CharField(max_length=150)

    def validate_nickname(self, value):
        # Ensuring the nickname isn't already in use
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This nickname is already taken")
        return value
