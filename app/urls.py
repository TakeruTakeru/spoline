
# -*- encoding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^linebot/', include('linebot.urls')),  # bot/ディレクトリへのルーティングを追加
]
