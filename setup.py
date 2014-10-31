import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'zbx-dashboard',
    version = '0.1.1',
    packages = ['zbx_dashboard'],
    include_package_data = True,
    license = 'MIT',
    description = 'Simple Django applicattion that provides an alternative to the Zabbix screens.',
    long_description = README,
    author = 'Vadym Kalsin',
    url = 'https://github.com/banzayats/zbx-dashboard/',
    author_email = 'neformat@gmail.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Monitoring',
    ],
    install_requires = [
        'Django',
        # 'MySQL-python',
        'pycurl>=7.19.0',
        'django-tinymce>=1.5',
        'django-admin-tools',
    ],
)