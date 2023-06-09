from django.contrib import admin

from .models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'mobile', 'check_out',
                    'datetime_checkin', 'datetime_checkout')
