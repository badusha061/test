from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Test(APIView):
    def get(self , request):
        data = "Hello World endha paripadi"
        return Response(data=data, status=status.HTTP_200_OK)
    