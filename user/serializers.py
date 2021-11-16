from rest_framework import serializers
from user.models import *
from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(required=True, allow_null=False)
	last_name = serializers.CharField(required=True, allow_null=False)
	email = serializers.CharField(required=True, allow_null=False)
	phone = serializers.CharField(required=True, allow_null=False)
	password = serializers.CharField(required=True, allow_null=False, write_only=True)
	address = serializers.CharField(required=True, allow_null=False)
	city = serializers.CharField(required=True, allow_null=False)
	state = serializers.CharField(required=True, allow_null=False)
	country = serializers.CharField(required=True, allow_null=False)
	
	class Meta:
		model = User
		fields = '__all__'
		extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class UserSupportSerializer(serializers.ModelSerializer):
	subscription = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = '__all__'


class UserProfileUpdateSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(required=False, allow_null=False)
	last_name = serializers.CharField(required=False, allow_null=False)
	email = serializers.CharField(allow_null=False, read_only=True)
	phone = serializers.CharField(required=False, allow_null=False)
	address = serializers.CharField(required=False, allow_null=False)
	city = serializers.CharField(required=False, allow_null=False)
	state = serializers.CharField(required=False, allow_null=False)
	country = serializers.CharField(required=False, allow_null=False)

	class Meta:
		model = User
		fields = [	'first_name',
					'last_name',
					'email',
					'phone',
					'address',
					'city',
					'state',
					'country',
				]
