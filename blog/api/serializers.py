from rest_framework import serializers
from .models import Post
# from serializers import ValidationError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        
        def validate(self, attrs):
            password=attrs.get('password')
            password2=attrs.pop('password2')
            if password != password2:
                raise ValidationError({"error":'password must match'})
            return attrs
        
        def create(self, validated_data):
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return user


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','content')