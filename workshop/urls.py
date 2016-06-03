from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.views import Home
admin.autodiscover()
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'workshop.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),    url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', Home.as_view(), name='home'),
                       )


