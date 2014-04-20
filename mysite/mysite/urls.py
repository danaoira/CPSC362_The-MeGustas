from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^dates/', include('dates.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^export/'. include('export')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$'. views.index, name='index')
)
