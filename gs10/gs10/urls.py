
from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView

# .router object
router = DefaultRouter()

router.register('singer' , views.Singerviewset , basename='singer' )
router.register('song' , views.Songviewset , basename='song' )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(router.urls)),
    

    path('auth/' , include('rest_framework.urls' , namespace='rest_framework'))

   


]
