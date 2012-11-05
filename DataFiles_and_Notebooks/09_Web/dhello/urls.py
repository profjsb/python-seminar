from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    # Examples:
    # url(r'^$', 'dhello.views.home', name='home'),
    # url(r'^dhello/', include('dhello.foo.urls')),
    ('^hello/$', 'views.hello'),
    (r'^$', 'views.hello'),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
