from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers


class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.all()
    serializer_class = serializers.PatientSerializer

