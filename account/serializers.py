from rest_framework import serializers
from .models import User

class Userserializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "name", "tc", "password", "password2"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        password = data.get("password")
        password2 = data.get("password2")

        if password != password2:
            raise serializers.ValidationError('Passwords do not match.')

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')  # Remove password2 from validated_data

        user = User.objects.create_user(password=password, **validated_data)

        return user


class LoginUserserializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=50)
    class Meta:
        model=User
        fields=['email','password']
        
        
class Userprofileserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','id','name']
        
class Userchangepasswordserializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        fields=['password','password2']
        
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        user=self.context.get('user')
        if password != password2:
            raise serializers.ValidationError('Passwords do not match.')
        user.set_password(password)
        user.save()

        return attrs
       