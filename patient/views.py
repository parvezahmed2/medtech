from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer 
    
    
#amar just post request korbo tai APIView use kori
class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer 
    
    def post(self, request):
        serializers = self.serializer_class(data=request.data) # data name er ekta attribute thake tar modde  request.data pass kore disi 
       
        if serializers.is_valid():
            user = serializers.save()
            return Response("done")
        return Response("done")     