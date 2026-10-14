
from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView
# .router object
# router = DefaultRouter()

# router.register('studentapi' , views.StudentModelViewSet , basename= 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('' , include(router.urls)),
    path('studentapi/' , views.StudentList.as_view()),
    path('studentapi/<int:pk>' , views.studentret.as_view()),

    # path('auth/' , include('rest_framework.urls' , namespace='rest_framework'))

    # token paths
    # path('access/' , TokenObtainPairView.as_view() , name='token_obtain_pair'),
    # path('refreshtoken/' , TokenRefreshView.as_view() , name='token_refresh'),
    # path('verifytoken/' , TokenVerifyView.as_view() , name='token_verify'),
    
    # path('auth/' , include('rest_framework.urls' , namespace='rest_framework'))
    




]
