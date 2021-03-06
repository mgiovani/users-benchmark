from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'created', 'email', 'name')
        read_only_fields = ('id', 'created')
