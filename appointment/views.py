from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class AppointmentViews(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()  # model thake sob gola object ekhane cole asbe 
    serializer_class = serializers.AppointmentSerizer  # model gola ke json convert kore 
    
    # custom query  kora 
    def get_queryset(self):
        queryset= super().get_queryset() # 7 no line ke niye aslma 
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
        