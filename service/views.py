from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers
from .models import bloodmodel
from .serializers import BloodModelSerializer, TestBookSerializer,TestModelSerializer

class ServiceViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()  # data query kore niye aste parbo
    serializer_class = serializers.ServiceSerializer  #query kora data ke json convert kora 

 


class BloodModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling all CRUD operations for bloodmodel.
    """
    queryset = bloodmodel.objects.all()
    serializer_class = BloodModelSerializer  
    


class TestBookView(viewsets.ModelViewSet):
    queryset = models.testBook.objects.all()
    serializer_class = TestBookSerializer

class TestModelView(viewsets.ModelViewSet):
    queryset = models.TestModel.objects.all()
    serializer_class = TestModelSerializer
    

