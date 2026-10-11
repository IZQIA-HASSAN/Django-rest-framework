
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_api/', views.student_api),
    path('stu_api/<int:pk>/', views.student_api),
]
