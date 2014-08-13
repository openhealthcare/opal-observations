"""
Urls for the OPAL observations plugin
"""
from django.conf.urls import patterns, url

from obs import views

urlpatterns = patterns(
    'obs',
    url('/chart/(?P<episode_id>[0-9]+)/?', views.ObsChartView.as_view()),
)
