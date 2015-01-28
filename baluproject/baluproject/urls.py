from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baluproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'inventory.views.home_page'),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^attributes/', include('attributes.urls')),
)
