
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_api/', views.StudentList_create.as_view()),
    
    path('stu_api/<int:pk>/', views.StudentRUD.as_view()),
]
