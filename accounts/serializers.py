from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



#user serailizer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields=('id','email', 'username')


#Register serializer 
class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields=('id','username','email', 'password')
		extra_kwargs={'password':{'write_only':True}}

	def create(self, validate_data):
		user = User.objects.create_user(validate_data['username'],
			validate_data['email'], validate_data['password'])
		return user

#login serializer 
class LoginSerializer(serializers.Serializer):
	username=serializers.CharField()
	password=serializers.CharField()

	def validate(self, data, *args, **kwargs):
		user=authenticate(**data)
		if user and user.is_active:
			return user 

		raise serializers.ValidationError("incorrect credentials")
