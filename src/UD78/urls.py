from django.conf.urls import include, url
from django.contrib import admin
import hammar

urlpatterns = [
    # Examples:
    # url(r'^$', 'UD78.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hammar/', include(hammar.urls)),
    
]
