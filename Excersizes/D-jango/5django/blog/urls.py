# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreatelView, BlogUpdateView, BlogDeleteView
# By using the period .views we reference the current directory, which is our pages app containing both views.py and urls.py

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), 
    # pk and id are interchangeable
    path('post/new/', BlogCreatelView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]