# coding: utf-8
from django.conf.urls import patterns, url

from zbx_dashboard.views import BoardListView, BoardDetailView
from zbx_dashboard.views import BoardCreateView, BoardUpdateView

urlpatterns = patterns(
    '',
    url(r'^$', BoardListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', BoardDetailView.as_view(), name='detail'),
    url(r'^add/$', BoardCreateView.as_view(), name='add'),
    url(r'^update/(?P<pk>\d+)/$', BoardUpdateView.as_view()),
)
