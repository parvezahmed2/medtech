from rest_framework import serializers
from . import models
class ServiceSerializer(serializers.ModelSerializer):  # model to json convert 
    class Meta:
        model = models.Service
        fields = '__all__'

class BloodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.bloodmodel
        fields = ['id', 'name', 'image', 'email', 'phone', 'bloodgroup'] 
        




class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestModel
        fields = ['id', 'name', 'image', 'cost']

# Serializer for the Appointment model
class TestBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.testBook
        fields = ['test', 'name', 'phone', 'email']
        
 
