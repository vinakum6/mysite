from django.contrib import admin
from django.urls import include, path
#Test
urlpatterns = [
    path(' ', include('polls.urls')),
    path('admin/', admin.site.urls),
]