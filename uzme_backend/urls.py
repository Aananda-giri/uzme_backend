"""uzme_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('devices', FCMDeviceAuthorizedViewSet)
from rest_framework.authtoken import views
from api.views import *

urlpatterns = [
    # URLs will show up at <api_root>/devices
    # DRF browsable API which lists all available endpoints
    path('api/', include(router.urls)), # for firebase notification
    path('admin/', admin.site.urls),
    path('api_auth/', include('api.urls', namespace='api')), # for authentication
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    # path('home/', index)
]

# import firebase_admin
# from firebase_admin import credentials, messaging
# firebase_cred = credentials.Certificate("firebase.json")
# firebase_app = firebase_admin.initialize_app(firebase_cred)

from fcm_django.models import FCMDevice
device = FCMDevice.objects.all().first()
device.send_message("Title", "Message")
device.send_message(data={"test": "test"})
device.send_message(title="Title", body="Message", icon=..., data={"test": "test"})

from firebase_admin import initialize_app
initialize_app(name=)