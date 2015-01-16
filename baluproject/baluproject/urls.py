from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baluproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'inventory.views.home_page'),
    url(r'^inventory/$', 'inventory.views.show_inventory_classes'),
    url(r'^inventory/(?P<id>\d{1,2})/edit.html$', 'inventory.views.edit_inventory'),
    url(r'^auth/', include('loginsys.urls')),
)
