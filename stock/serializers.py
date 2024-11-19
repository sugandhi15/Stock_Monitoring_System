from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # write_only ensures that field is only write and cannot be readed

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        # Create a new user and hash the password automatically
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # This hashes the password
        user.save()
        return user