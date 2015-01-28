# coding: utf-8

"""
Django settings for zabbix_dashboard project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SeCreTKeY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'tinymce',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jenkins',
	'django_nose',
    'zbx_dashboard',
    'debug_toolbar.apps.DebugToolbarConfig',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zabbix_dashboard.urls'

WSGI_APPLICATION = 'zabbix_dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = ()

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

# django-nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Django Debug Toolbar
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1',)

# Used by decorator login_required()
LOGIN_REDIRECT_URL = '/boards'

# Jenkins settings
PROJECT_APPS = ('zbx_dashboard',)

JENKINS_TASKS = ('django_jenkins.tasks.run_pylint',
                 'django_jenkins.tasks.run_pep8',
                 'django_jenkins.tasks.run_pyflakes',
)

# Zabbix credentials
ZABBIX_URL = 'https://zabbix.org/zabbix/'
ZABBIX_USER = 'zabbix_user'
ZABBIX_PASS = 'pa$$w0rd'

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

# Admin Tools
ADMIN_TOOLS_INDEX_DASHBOARD = 'zabbix_dashboard.dashboard.CustomIndexDashboard'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)