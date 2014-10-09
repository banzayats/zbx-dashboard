# coding: utf-8

from django.contrib import admin
from zbx_dashboard.models import Board, Graph
from django.utils.translation import ugettext as _


class GraphInline(admin.TabularInline):
    model = Graph
    extra = 3
    verbose_name = _(u'Graphs')


class BoardAdmin(admin.ModelAdmin):    # pylint: disable=R0904
    fieldsets = [
        (
            None,
            {'fields': ['title']}
        ),
        (
            _(u'Dashboard options'),
            {'fields': [('description', 'groups'), ], 'classes': ['collapse']}
        ),
    ]
    inlines = [GraphInline]
    list_display = ('title', 'description', 'get_groups')

admin.site.register(Board, BoardAdmin)
