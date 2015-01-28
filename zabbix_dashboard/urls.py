from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zabbix_dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^$', include('zbx_dashboard.urls')),
    url(r'^boards/', include('zbx_dashboard.urls', namespace="boards")),
    url(r'^accounts/login/$',  login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^tinymce/', include('tinymce.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )