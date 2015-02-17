from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from views import splash, home, about, friend, contest1, contest2, contest3

urlpatterns = patterns('',
                       url(r'^$', splash),
                       url(r'^home', home),
                       url(r'^about', 'Agency.views.about', name='about'),
                       url(r'^friend', 'Agency.views.friend', name='friend'),
                       url(r'^contest1', 'Agency.views.contest1',
                           name='contest1'),
                       url(r'^contest2', 'Agency.views.contest2',
                           name='contest2'),
                       url(r'^contest3', 'Agency.views.contest3',
                           name='contest3'),
                       url(r'^thanks', 'Agency.views.thanks', name='thanks'),
                       url(r'^services', 'Agency.views.services',
                           name='services'),
                       url(r'^contact', 'Agency.views.contact',
                           name='contact'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
