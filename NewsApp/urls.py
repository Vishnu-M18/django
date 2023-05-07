from django.contrib import admin
from django.urls import path, include  #add
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MainApp.urls')), #add
]