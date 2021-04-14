from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls'))
]

if not settings.DEBUG: urlpatterns += [ url(r'^uploads/(?P<path>.)$', serve,{'document_root': settings.MEDIA_ROOT}), url(r'^static/(?P<path>.)$', serve,{'document_root': settings.STATIC_ROOT}), ]