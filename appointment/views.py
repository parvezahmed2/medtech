from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
# class AppointmentViews(viewsets.ModelViewSet):
#     queryset = models.Appointment.objects.all()
#     serializer_class = serializers.AppointmentSerizer
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         doctor_id = self.request.query_params.get('doctor_id')
#         status = self.request.query_params.get('status')
        
        
#         if doctor_id:
#             queryset = queryset.filter(doctor_id=doctor_id)
#         if status:
#             queryset = queryset.filter(appointment_status=status)
#         return queryset

from rest_framework import viewsets
from . import models, serializers

from rest_framework.response import Response
from rest_framework import status

class AppointmentViews(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class =serializers.AppointmentSerizer
    