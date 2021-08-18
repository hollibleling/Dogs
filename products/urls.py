from django.urls import path

from products.views import SampleView
from products.views import DogView

urlpatterns = [
	path('', SampleView.as_view()),
    path('dog/', DogView.as_view()), 
]