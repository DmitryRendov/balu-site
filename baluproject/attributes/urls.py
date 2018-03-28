from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baluproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'attributes.views.attributes'),
    url(r'^(?P<id>\d{1,2})/edit.html$', 'attributes.views.edit_attribute'),
    url(r'^(?P<id>\d{1,2})/delete.html$', 'attributes.views.delete_attribute'),
    url(r'^add.html$', 'attributes.views.add_attribute'),
)
