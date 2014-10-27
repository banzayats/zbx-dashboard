# coding: utf-8
# pylint: disable=unexpected-keyword-arg, no-value-for-parameter

from django import forms
from django.utils.translation import ugettext as _

# Form to select the time interval


class SelectForm(forms.Form):
    CHOICES = (
        ('86400', _("1 day")),
        ('3600', _("1 hour")),
        ('7200', _("2 hours")),
        ('10800', _("3 hours")),
        ('21600', _("6 hours")),
        ('43200', _("12 hours")),
        ('604800', _("1 week")),
        ('1209600', _("2 weeks")),
        ('2592000', _("1 month")),
        ('7776000', _("3 months")),
        ('15552000', _("6 months")),
        ('31536000', _("Year")),
    )

    select = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control input-sm',
                'onchange': 'this.form.submit();',
            }
        ),
        choices=CHOICES,
        label=_("Zoom"),
    )
