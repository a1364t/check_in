from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Visitor
from .forms import VisitorForm


class VisitorListView(generic.ListView):
    model = Visitor
    template_name = 'visitors/visitors_list.html'
    context_object_name = 'visitors_list'

    def get_queryset(self):
        return Visitor.objects.all().order_by('-datetime_checkin')


class VisitorDetailView(generic.DetailView):
    model = Visitor
    form_class = VisitorForm
    template_name = 'visitors/visitor_detail.html'
    context_object_name = 'visitor'


class VisitorCreateView(generic.CreateView):
    form_class = VisitorForm
    template_name = 'visitors/visitor_create.html'
    success_url = reverse_lazy('visitors_list')


class VisitorUpdateView(generic.UpdateView):
    form_class = VisitorForm
    template_name = 'visitors/visitor_create.html'
    model = Visitor


class VisitorDeleteView(generic.DeleteView):
    model = Visitor
    template_name = 'visitors/visitor_delete.html'
    success_url = reverse_lazy('visitors_list')
