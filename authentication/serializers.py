# authentication/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'mobile_number', 'profile_image')
        extra_kwargs = {
            'profile_image': {'required': False},
            'date_of_birth': {'required': False},
            'mobile_number': {'required': False},
        }


class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        validated_data.pop('password2')  # Remove the confirm password field
        user = User.objects.create_user(**validated_data)
        Profile.objects.update_or_create(user=user, defaults=profile_data)
        return user