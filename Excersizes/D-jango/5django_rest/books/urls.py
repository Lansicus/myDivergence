from django.urls import path
from .views import BookListView

urlpatterns = [
    
    path('', BookListView.as_view(), name='home'), # Letting the project know of the book app
]