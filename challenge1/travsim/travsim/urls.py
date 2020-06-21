"""travsim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import include, url
from django.contrib import admin

from restapi import views

admin.autodiscover()

# urlpatterns = [
#   path("admin/", admin.site.urls),
#   path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
#   # path("Goods/", include("Goods.urls", namespace="goods")),
#   # path("Goods/", include("GoodsDetail.urls", namespace="goods_details")),
#   path(r'^Goods/, views.Goods.as_view()),
#   path(r'^Goods/(?P<pk>[0-9]+)/$', views.GoodsDetail.as_view()),
# ]

urlpatterns = [
  url(r'^admin/', include(admin.site.urls)),
  url(r'^api-auth/', include('rest_framework', namespace='rest_framework')),
  url(r'^goods/', views.Goods.as_view()),
  url(r'^goods/(?P<pk>[0-9]+)/$', views.GoodsDetail.as_view())]
