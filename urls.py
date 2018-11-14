from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deneme.views.home', name='home'),
    url(r'^blog/', include('blog.url1ss')),

    url(r'^admin/', include(admin.site.urls)),
)
