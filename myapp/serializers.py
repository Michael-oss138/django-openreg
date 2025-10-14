from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']  

    def create(self, validated_data):
        password =self.validated_data.pop('password')
        user = User.objects.create_user(password=password, **self.validated_data)

        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get('username')
        password = attrs.get('password')

        user = None
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                user = authenticate(email=user.email, password=password)

            except User.DoesNotExist:
                pass

        else:
            user = authenticate(email=username_or_email, password=password)
            if user is None:
                raise serializers.ValidationError('Invalid Credentials or Invalid account')


        data = super().validate(attrs)
        data['user'] = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name
        }
        return data