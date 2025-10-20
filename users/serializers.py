from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True , min_length=8)
  password2 = serializers.CharField(write_only=True , min_length=8)

  class Meta:
    model = User
    fields = ['username','email','password','password2']

  def validate(self , data):
    if data['password']!=data['password2']:
      raise serializers.ValidationError({"password":"Passwords dont match"})
    return data
  
  def create(self , validated_data):
    validated_data.pop('password2')
    password = validated_data.pop('password')

    # Create the user and hash password with set_password
    user = User(**validated_data)
    user.set_password(password)
    user.save()
    return user
  

  
class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('id', 'username', 'email')
      read_only_fields = ('id', 'username', 'email')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)
    data.update({
      "user":UserSerializer(self.user).data
    })
    return data