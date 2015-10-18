from django.conf.urls import include, url
from django.contrib import admin
from Daten2 import views


urlpatterns = [
    url(r'^$', views.start, name ='start'),           
    url(r'^', include('django.contrib.auth.urls')),
    url(r'logout/$',views.logout),
    url(r'login/$',views.login),   
    url(r'projekt/(?P<nummer>\d+)/$', views.edit_Projekt),
    url(r'projekt/neu/(?P<klasseid>\d+)/$', views.neues_Projekt),
    url(r'Indexleiste/$', views.indexleiste),
    url(r'index/$',views.index),
    url(r'^ShowLehrer/(?P<sortierung>[a-z])/$',views.showlehrer),   
    url(r'^ShowRaum/$',views.showraum), 
    url(r'projekt/(?P<nummer>\d+)/Druckversion/$', views.ProjektDruckversion),
]
