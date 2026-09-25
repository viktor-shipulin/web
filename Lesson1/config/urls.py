from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from event_hub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.event_list),
    path('create/', views.event_create),
    path('<int:pk>/', views.event_detail),
    path('<int:pk>/edit/', views.event_update),
    path('<int:pk>/delete/', views.event_delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)