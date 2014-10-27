.. image:: https://pypip.in/download/zbx-dashboard/badge.svg
    :target: https://pypi.python.org/pypi/zbx-dashboard/
    :alt: Downloads
.. image:: https://pypip.in/version/zbx-dashboard/badge.svg
    :target: https://pypi.python.org/pypi/zbx-dashboard/
    :alt: Latest Version
.. image:: https://travis-ci.org/banzayats/zbx-dashboard.svg?branch=master
    :target: https://travis-ci.org/banzayats/zbx-dashboard
    :alt: Travis CI

===============================================
zbx_dashboard
===============================================
`zbx_dashboard` is a simple Django applicattion that provides an alternative to the Zabbix screens.
It allows users who are not registered in Zabbix being able to view the graphs and (in the future) more data from Zabbix.

Prerequisites
===============================================
- Django 1.5.*, 1.6.*, 1.7.*
- Python 2.6.8+, 2.7.*

Main features
===============================================
- Group graphs in separate dashboards
- Rearrange graphs on the dashboard
- Each dashboard and the graph can be provided a brief description
- Dashboards may belong to different groups of users

Installation
===============================================
1. Install latest stable version from PyPI:

.. code-block:: none

    $ pip install zbx-dashboard

Or latest stable version from GitHub:

.. code-block:: none

    $ pip install -e git+https://github.com/banzayats/zbx-dashboard@stable#egg=zbx-dashboard

2. Edit your projects' Django settings:

.. code-block:: python

    INSTALLED_APPS = (
        'admin_tools',
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'tinymce',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'zbx_dashboard',
    )

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    LOGIN_REDIRECT_URL = '/boards'

    # Set up your Zabbix server credentials
    ZABBIX_URL = 'https://zabbix.org/zabbix/'
    ZABBIX_USER = 'guest'
    ZABBIX_PASS = ''

    # TinyMCE
    TINYMCE_DEFAULT_CONFIG = {
        'mode': 'exact',
        'theme': "advanced",
        'relative_urls': False,
        'width': 400,
        'height': 200,
        'plugins': 'inlinepopups,preview,media,contextmenu,paste,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras',
        'theme_advanced_buttons1': 'fullscreen,|,bold,italic,underline,strikethrough,|,sub,sup,|,bullist,numlist,|,outdent,indent,|,formatselect,removeformat,|,preview,code',
        'theme_simple_toolbar_location': 'top',
        'theme_advanced_toolbar_align': 'left',
    }

    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
    )

3.  Add to urls.py:

.. code-block:: python

    from django.contrib.auth.views import login, logout

    urlpatterns = patterns('',
        # ...
        url(r'^admin_tools/', include('admin_tools.urls')),
        url(r'^boards/', include('zbx_dashboard.urls', namespace="boards")),
        url(r'^accounts/login/$',  login, name='login'),
        url(r'^accounts/logout/$', logout, name='logout'),
        url(r'^tinymce/', include('tinymce.urls')),
    )

4. Run:

.. code-block:: none

    $ python manage.py syncdb

This creates a few tables in your database that are necessary for operation.

5. Make ``static`` directory in your projects' root directory and run:

.. code-block:: none

    $ python manage.py collectstatic

6. Test the application. Run the development server:

.. code-block:: none

    $ python manage.py runserver 0.0.0.0:5000

Demo
===============================================
Demo site: http://boyard.pp.ua

login: admin, password: admin 
