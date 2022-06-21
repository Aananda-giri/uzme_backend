from django.urls import path, include
from django.views.generic import TemplateView
from .views import UserRecordView

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path("firebase-messaging-sw.js",        # for notifications
        TemplateView.as_view(
            template_name="firebase-messaging-sw.js",
            content_type="application/javascript",
        ),
        name="firebase-messaging-sw.js"
    ),
]
