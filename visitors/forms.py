from django import forms
from .models import Visitor


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'family', 'mobile', 'email', 'visiting_staff']
        exclude = []
