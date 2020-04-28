from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^client/$', views.client_list),
    url(r'^client/(?P<pk>[0-9]+)$', views.client_detail),
    url(r'^rasp/$', views.rasp_list),
    url(r'^rasp/(?P<pk>[0-9]+)$', views.rasp_detail),
]