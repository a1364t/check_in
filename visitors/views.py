from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Visitor
from .forms import VisitorForm


class VisitorCreateView(generic.CreateView):
    model = VisitorForm
    template_name = 'visitors/visitor_create.html'


class VisitorUpdateView(generic.UpdateView):
    form_class = VisitorForm
    template_name = 'visitors/visitor_update.html'
    model = Visitor
