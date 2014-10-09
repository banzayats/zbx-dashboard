# coding: utf-8
from django.conf.urls import patterns, url

from zbx_dashboard.views import BoardListView, BoardDetailView

urlpatterns = patterns(
    '',
    url(r'^$', BoardListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', BoardDetailView.as_view(), name='detail'),
)
