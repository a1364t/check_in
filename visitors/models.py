from django.db import models
from django.shortcuts import reverse


class Visitor(models.Model):

    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    check_out = models.BooleanField(default=False, null=True, blank=True)
    datetime_checkin = models.DateTimeField(auto_now_add=True)
    datetime_checkout = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse('visitors_list')
