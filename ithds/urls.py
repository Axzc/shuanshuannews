from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('tinymce', include('tinymce.urls')),
    path('user', include(('apps.user.urls', "apps.user"), namespace="user")),
    path('', include(('apps.goods.urls', 'apps.goods'), namespace="goods"))
]

