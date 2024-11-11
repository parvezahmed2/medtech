from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate 
from rest_framework.authtoken.models import Token

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
    

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)  # user jei data diye request korbe 
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username = username, password = password)
            if user:
                token, _ = Token.objects.get_or_create(user = user)  # ei username or pass diye kono token database ase ki na 
                return Response({'token': token.key, 'user_id': user.id}) 
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors) 



 