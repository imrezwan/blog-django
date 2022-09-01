from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name = 'home'),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name = 'post-detail'),
    path('about/', views.BlogListView.as_view(), name = 'aboutus')
]
