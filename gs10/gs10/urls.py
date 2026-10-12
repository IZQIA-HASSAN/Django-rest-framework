
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stu_api/', views.StudentList.as_view()),
    path('stu_api/', views.StudentLC.as_view()),
    # path('stu_api/', views.Studentcreate.as_view()),
    
    # path('stu_api/<int:pk>/', views.StudentRUD.as_view()),
    # path('stu_api/<int:pk>/', views.studentret.as_view()),
    # path('stu_api/<int:pk>/', views.Studentupd.as_view()),
    # path('stu_api/<int:pk>/', views.Studentdes.as_view()),
    # path('stu_api/<int:pk>/', views.StudentRU.as_view()),
    path('stu_api/<int:pk>/', views.StudentRD.as_view()),
]
