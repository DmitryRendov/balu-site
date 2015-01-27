from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baluproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'inventory.views.show_inventory_classes', name='index'),
    url(r'^(?P<id>\d{1,2})/edit.html$', 'inventory.views.edit_inventory'),
    url(r'^(?P<id>\d{1,2})/delete.html$', 'inventory.views.delete_inventory'),
    url(r'^add.html$', 'inventory.views.add_inventory'),
    url(r'^(?P<id>\d{1,2})/attributes.html$', 'inventory.views.attributes'),
)
