# coding: utf-8

from django import template

register = template.Library()


@register.filter
def get_img_period(obj, period):
    return obj.get_b64_img(period)
