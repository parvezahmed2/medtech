from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # router [get post update delete]
router.register('', views.ContactViewset) # router er antena 

urlpatterns = [
    path('', include(router.urls)),   
]

