from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.CheckInView.as_view(), name='signup'),
]
