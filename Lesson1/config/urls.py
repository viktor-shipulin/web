from django.contrib import admin
from django.urls import path
from event_hub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.event_list),
]