
from django.contrib import admin
from django.urls import path
from myapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.hello_world),
]
