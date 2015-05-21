'''
Created on 2015-5-12

@author: user
'''
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^stock_list/', views.list_stock,),
    #url(r'^admin/', include(admin.site.urls)),
]