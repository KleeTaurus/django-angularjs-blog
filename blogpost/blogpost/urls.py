from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'blogpost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api', include('blogpost_api.urls')),
    url(r'^', include('blogpost_web.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
