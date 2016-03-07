from django.conf.urls import patterns, include, url
from django.contrib import admin


# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'pygrow.views.index', name='index'),
#     # url(r'^$', 'monitoring.views.index', name='index'),

#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = [
    url(r'^monitoring/', include('monitoring.urls')),
    url(r'^admin-only/', admin.site.urls, name='admin'),
]
