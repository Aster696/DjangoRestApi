from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=225, min_length=4)
    first_name = serializers.CharField(max_length=225, min_length=2, write_only=True)
    last_name = serializers.CharField(max_length=225, min_length=2, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        if User.objects.filter(email = attrs['email']).exists():
            raise serializers.ValidationError({'email': ('Email already exist')})
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)