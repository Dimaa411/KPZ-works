from django.urls import path
from myapp.views import index
from django.contrib import admin


urlpatterns = [
    path('', index, name='home'),
    path('admin', admin.site.urls),
]
