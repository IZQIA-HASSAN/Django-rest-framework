
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_api/', views.StudentList.as_view()),
    # path('stu_api/', views.Studentcreate.as_view()),
    # path('stu_api/', views.Studentret.as_view()),
    # path('stu_api/<int:pk>/', views.Studentret.as_view()),
    # path('stu_api/<int:pk>/', views.Studentupd.as_view()),
    path('stu_api/<int:pk>/', views.Studentdel.as_view()),
]
