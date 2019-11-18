from django.shortcuts import render
from .models import AccountModel
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import *

@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes((JSONParser, ))
def login(request):
    data = request.data
    data.pop('type')
    print(data)
    serializer = LoginSerializer(data=data, context={'request': request})
    if not serializer.is_valid():
        return Response({'error': 'blank username or password'}, status=401)
        # return Response(serializer.errors)
    user = get_object_or_404(AccountModel,email=serializer.validated_data['email'])
    if not user.check_password(serializer.validated_data['password']):
        return Response({'error': 'Incorrect username or password'}, status=401)
    serializer = UserLoginSerializer(user)
    data = serializer.data
    print(data)
    return Response(data)