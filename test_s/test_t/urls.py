from django.contrib import admin
from django.urls import path
from .views import send_email_view
from .views import *

app_name = 'test_t'

urlpatterns = [
    path('admin/', admin.site.urls),
     path('send-email/', send_email_view, name='send-email'),
]