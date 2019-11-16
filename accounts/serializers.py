from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from .models import AccountModel

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    password = serializers.CharField()

class AccountSerializer(ModelSerializer):
	token = serializers.SerializerMethodField()
	class Meta:
	    model=AccountModel
	    fields=('email','name','date_joined','is_active','is_staff','token','department','role','phone')
    
class UserLoginSerializer(AccountSerializer):
    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token