from django.conf.urls import patterns, include, url
from courses import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TitanPlanner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^display-all/', views.display_all, name='display_all'),
	url(r'^calendar/', views.calendar, name='calendar'),
	url(r'^add/(?P<pk>\w+)/$', views.add, name='add'),
	url(r'^remove/(?P<pk>\w+)/$', views.remove, name='remove'),
	url(r'^search/$', views.search, name='search'),
	url(r'^search-form/$', views.search_form, name='search_form'),
    url(r'^admin/', include(admin.site.urls) )
)
