from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

from .models import Visitor
from .forms import VisitorForm


class VisitorListView(generic.ListView):
    model = Visitor
    template_name = 'visitors/visitors_list.html'
    context_object_name = 'visitors_list'

    def get_queryset(self):
        return Visitor.objects.all().order_by('-datetime_checkin')


class AllVisitotrListView(LoginRequiredMixin, generic.ListView):
    model = Visitor
    paginate_by = 10
    template_name = 'visitors/all_visitors_list.html'
    context_object_name = 'visitors_list'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

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

    def form_valid(self, form):
        visitor = form.save()
        messages.success(
            self.request, f"Thank you {visitor.name}, you have successfully checked in! An email has been sent to you!")
        response = super().form_valid(form)
        self.welcome_email(visitor.email)
        return response

    def welcome_email(self, email_reciever):
        subject = 'Hello'
        message = 'This is a test email'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email_reciever]

        pdf_path = './static/myfiles/welcome.pdf'

        email = EmailMessage(subject, message, from_email, recipient_list)
        with open(pdf_path, 'rb') as file:
            email.attach('welcome.pdf', file.read(), 'application/pdf')
        email.send()


class VisitorUpdateView(generic.UpdateView):
    model = Visitor
    form_class = VisitorForm
    template_name = 'visitors/visitor_update.html'
    success_url = reverse_lazy('visitors_list')

    def form_valid(self, form):
        visitor = form.save(commit=False)
        visitor.check_out = True

        messages.success(
            self.request, f"Thank you {visitor.name} for visiting!")

        return super().form_valid(form)


class VisitorDeleteView(generic.DeleteView):
    model = Visitor
    template_name = 'visitors/visitor_delete.html'
    success_url = reverse_lazy('visitors_list')
