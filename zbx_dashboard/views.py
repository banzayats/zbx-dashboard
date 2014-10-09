# coding: utf-8
# pylint: disable=unexpected-keyword-arg, no-value-for-parameter

from zbx_dashboard.models import Board
from zbx_dashboard.forms import SelectForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class BoardListView(ListView):
    """
    List of all available dashboards
    """
    model = Board
    template_name = 'zbx_dashboard/list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BoardListView, self).dispatch(request, *args, **kwargs)

    # Filter dashboards by current user group id
    def get_queryset(self):
        try:
            user_id = self.request.user.groups.all()[0].id
        except IndexError:
            user_id = 0
        return Board.objects.filter(
            groups__id=user_id
        )


class BoardDetailView(DetailView):
    """
    Dashboard view
    """
    model = Board
    template_name = 'zbx_dashboard/detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BoardDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BoardDetailView, self).get_context_data(**kwargs)
        context['form'] = SelectForm(initial=self.request.GET)
        context['period'] = self.request.GET.get('select', 86400)
        return context

    # Prevent user changing URL <pk> to see other dashboards
    def get_queryset(self):
        try:
            user_id = self.request.user.groups.all()[0].id
        except IndexError:
            user_id = 0
        return Board.objects.filter(
            groups__id=user_id
        )
