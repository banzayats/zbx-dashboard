# coding: utf-8

from django.db import models
from django.contrib.auth.models import Group
from tinymce import models as tinymce_models
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
import base64
from StringIO import StringIO
import sys
sys.path.append('/usr/lib64/python2.6/site-packages/')
import pycurl


class Board(models.Model):
    title = models.CharField(
        verbose_name=_(u'Title'),
        max_length=255
    )
    description = models.TextField(
        verbose_name=_('Short description'),
        max_length=1000,
        blank=True,
        null=True
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        verbose_name=_('Linked groups'),
    )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/boards/%i/" % self.id

    def get_groups(self):
        return ", ".join([p.name for p in self.groups.all()])
    get_groups.short_description = _('Linked groups')

    class Meta:
        verbose_name = _('Board')
        verbose_name_plural = _('Boards')


class Graph(models.Model):
    widget = models.ForeignKey(Board)
    title = models.CharField(
        verbose_name=_(u'Title'),
        max_length=255
    )
    graph_id = models.CharField(
        verbose_name=_(u'Graph ID'),
        max_length=8
    )
    description = tinymce_models.HTMLField(
        verbose_name=_(u'Graph description'),
        max_length=1000,
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.title

    def get_b64_img(self, period=86400):
        buff = StringIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.COOKIEFILE, "")
        curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        login_url = settings.ZABBIX_URL + 'index.php?login=1'
        curl.setopt(pycurl.URL, login_url)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(
            pycurl.HTTPPOST,
            [
                ('name', settings.ZABBIX_USER),
                ('password', settings.ZABBIX_PASS),
                ('enter', 'Sign in'),
                ('autologin', '1'),
                ('request', '')
            ]
        )
        curl.perform()
        curl.setopt(pycurl.POST, 0)
        img_url = settings.ZABBIX_URL + 'chart2.php?graphid=' + \
            str(self.graph_id) + '&width=400&height=200&period=' + str(period)
        curl.setopt(pycurl.URL, img_url)
        curl.setopt(pycurl.WRITEFUNCTION, buff.write)
        curl.perform()
        img = buff.getvalue()
        buff.close()
        curl.close()
        return "data:image/jpg;base64,%s" % base64.b64encode(img)

    class Meta:
        verbose_name = _('Graph')
        verbose_name_plural = _('Graphs')
