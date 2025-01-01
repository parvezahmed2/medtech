from django.contrib import admin
from .models import Service,bloodmodel, TestModel, testBook
# Register your models here.

admin.site.register(Service)
admin.site.register(bloodmodel)
admin.site.register(TestModel)
admin.site.register(testBook)