from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^monitoring/', include('monitoring.urls')),
    # url(r'^admin/', admin.site.urls),

    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # url(r'^dashboard/$', views.dashboard, name='dashboard'),

    url(r'^camera/$', views.CameraView.as_view(), name='camera'),
    url(r'^temperature/$', views.TemperatureView.as_view(), name='temperature'),
    url(r'^humidity/$', views.HumidityView.as_view(), name='humidity'),

    # url(r'^jobs/$', views.JobsView.as_view(), name='jobs'),

    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
]
