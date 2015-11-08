from django.conf.urls import patterns, include, url

urlpatterns = patterns('accomodation.views',

    url(r'^$', 'accomodation', name='accomodation'),
    url(r'^check-available/$', 'checkavailable', name='checkavailable'),

)

