from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # router [get post update delete]
router.register('help', views.ServiceViewset) # router er antena 
router.register('blood', views.BloodModelViewSet) # router er antena 
router.register('testbook', views.TestBookView) # router er antena 
router.register('test', views.TestModelView) # router er antena 

urlpatterns = [
    path('', include(router.urls)),   
]
