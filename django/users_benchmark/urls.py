import rest_framework
from django.contrib import admin
from django.urls import path

from users.views import UserView

urlpatterns = [
    path('', UserView.as_view(), name='users'),
    path('admin/', admin.site.urls),
]
