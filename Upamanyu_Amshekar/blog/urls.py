from django.urls import path
from .views import home

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='index'),
    path('image_upload', views.hotel_image_view, name='image_upload'),
    path('success', views.success, name='success'),
    path('transform_img', views.transform_img, name='transform_img'),
    path('rgb2gray', views.rgb2gray, name='rgb2gray'),
    path('rgb2bin', views.rgb2bin, name='rgb2bin'),
    path('rgb2red', views.rgb2red, name='rgb2red'),
    path('rgb2log', views.rgb2log, name='rgb2log'),
    path('rgb2logi', views.rgb2logi, name='rgb2logi'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)