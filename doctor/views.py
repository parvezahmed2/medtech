from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers


class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.all()
    serializer_class = serializers.SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.all()
    serializer_class = serializers.DesignationSerializer

class AvailableViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.all()
    serializer_class = serializers.AvailableTimeSerializer

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.all()
    serializer_class = serializers.DoctorSerializer


class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.all()
    serializer_class = serializers.ReviewSerializer

