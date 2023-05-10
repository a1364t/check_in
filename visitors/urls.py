from django.urls import path
from . import views


urlpatterns = [
    path('', views.VisitorListView.as_view(), name='visitors_list'),
    path('<int:pk>/', views.VisitorDetailView.as_view(), name='visitor_detail'),
    path('create/', views.VisitorCreateView.as_view(), name='visitor_create'),
    path('<int:pk>/update/', views.VisitorUpdateView.as_view(),
         name='visitor_update'),
    path('<int:pk>/delete', views.VisitorDeleteView.as_view(), name='visitor_delete'),
]
