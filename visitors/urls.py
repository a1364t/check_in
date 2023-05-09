from django.urls import path
from . import views


urlpatterns = [
    path('', views.VisitorCreateView.as_view(), name='visitor_create'),
    path('delete/', views.VisitorUpdateView.as_view(), name='visitor_update'),
]
