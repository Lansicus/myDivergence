from django.urls import path
from .views import BookAPIView

urlpatterns = [
    
    path('', BookAPIView.as_view()), # Letting the project know of the book app
]