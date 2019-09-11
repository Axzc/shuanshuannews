from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^user/', include('apps.user.urls', namespace='user')),
    url(r'^', include('apps.goods.urls', namespace='goods'))
]

