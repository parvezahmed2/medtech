from rest_framework import serializers
from . import models 


# class AppointmentSerizer(serializers.ModelSerializer):
#     time = serializers.StringRelatedField(many = False)
#     doctor = serializers.StringRelatedField(many = False)
#     class Meta:
#         model = models.Appointment
#         fields = '__all__'

class AppointmentSerizer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'
