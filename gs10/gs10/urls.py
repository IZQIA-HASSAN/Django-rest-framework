
from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter

# .router object
router = DefaultRouter()

# register student view set with router

router.register('studentapi' , views.StudentView , basename= 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(router.urls))
    
    # path('stu_api/', views.StudentLC.as_view()),
    
    # path('stu_api/<int:pk>/', views.StudentRUD.as_view()),




]
