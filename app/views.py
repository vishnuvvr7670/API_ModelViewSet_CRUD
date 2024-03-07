from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class ProdutCrud(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer