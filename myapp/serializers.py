from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']  

        def create(self, validated_date):
            password = validated_data.pop('password')
            user = User.objects.create_user(password=password, **validated_data)

            user.save()
            return user