
from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# .router object
router = DefaultRouter()

# register student view set with router

# router.register('studentapi' , views.StudentView , basename= 'student')

# same router for model viewsets
router.register('studentapi' , views.StudentModelViewSet , basename= 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(router.urls)),
    path('auth/' , include('rest_framework.urls' , namespace='rest_framework')),
    # path('gettoken/' , obtain_auth_token)
    
    # path('stu_api/', views.StudentLC.as_view()),
    
    # path('stu_api/<int:pk>/', views.StudentRUD.as_view()),




]
