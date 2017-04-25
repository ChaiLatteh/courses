from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^remove_confirm/(?P<id>\d+)$', views.remove_confirm)
]
