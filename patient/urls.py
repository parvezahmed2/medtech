from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # router [get post update delete]
router.register('list', views.PatientViewset) # router er antena 

urlpatterns = [
    path('', include(router.urls)),   
    path('register/', views.UserRegistrationApiView.as_view(), name = 'register'),
    path('login/', views.UserLoginApiView.as_view(), name='login')
]
