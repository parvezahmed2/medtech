from django.urls import include, path
from rest_framework import routers
from . import views 

router = routers.DefaultRouter()  # router toiri kor holo 

router.register('', views.AppointmentViews)  # entena  toiri hoise [get post update delete] 

urlpatterns = [
    path('', include(router.urls)),   
]


