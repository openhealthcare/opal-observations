"""
Urls for the Opal observations plugin
"""
from django.conf.urls import url

from obs import views

urlpatterns = [
#    'obs',
    url('/chart/(?P<episode_id>[0-9]+)/?', views.ObsChartView.as_view()),
]
