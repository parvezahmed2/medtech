from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers


class ServiceViewset(viewsets.ModelViewSet):
    queryset = models.Service.all()  # data query kore niye aste parbo
    serializer_class = serializers.ServiceSerializer  #query kora data ke json convert kora 
