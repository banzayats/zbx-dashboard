# coding: utf-8
# pylint: disable=unexpected-keyword-arg, no-value-for-parameter

from zbx_dashboard.models import Board
from zbx_dashboard.forms import SelectForm, GraphFormSet, BoardForm
from zbx_dashboard.utils import zbx_get_graphs, zbx_get_screen_name
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect


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


class BoardCreateView(CreateView):
    model = Board
    template_name = 'zbx_dashboard/add.html'
    form_class = BoardForm

    def __init__(self):
        self.object = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BoardCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        screen_id = self.request.GET.get('screen_id')
        initials = zbx_get_graphs(screen_id)  # get inital items from zabbix
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.initial = {'title': zbx_get_screen_name(screen_id)}
        graph_form = GraphFormSet()
        graph_form.extra = len(initials) + 1
        for subform, data in zip(graph_form.forms, initials):
            subform.initial = data
        return self.render_to_response(
            self.get_context_data(form=form, graph_form=graph_form)
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        graph_form = GraphFormSet(self.request.POST)
        if form.is_valid() and graph_form.is_valid():
            return self.form_valid(form, graph_form)
        else:
            return self.form_invalid(form, graph_form)

    def form_valid(self, form, graph_form):
        """
        Called if all forms are valid. Creates a Board instance along with
        associated Graphs and then redirects to a success page.
        """
        self.object = form.save()
        graph_form.instance = self.object
        graph_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, graph_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, graph_form=graph_form)
        )


class BoardUpdateView(UpdateView):
    model = Board
    template_name = 'zbx_dashboard/update.html'
    form_class = BoardForm

    def __init__(self):
        self.object = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BoardUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BoardUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['graph_form'] = GraphFormSet(self.request.POST,
                                                 instance=self.object)
        else:
            context['graph_form'] = GraphFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        context = self.get_context_data()
        graph_form = context['graph_form']
        if graph_form.is_valid():
            self.object = form.save()
            graph_form.instance = self.object
            graph_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    # Prevent user changing URL <pk> to see other dashboard
    def get_queryset(self):
        try:
            user_id = self.request.user.groups.all()[0].id
        except IndexError:
            user_id = 0
        return Board.objects.filter(
            groups__id=user_id
        )
