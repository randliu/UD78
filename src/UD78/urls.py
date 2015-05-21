from django.conf.urls import include, url
from django.contrib import admin
import titan

urlpatterns = [
    # Examples:
    # url(r'^$', 'UD78.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^titan/', include(titan.urls)),
    
]
