from django.contrib import admin
from django.urls import path

from config import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.default_view, name='default')
]
