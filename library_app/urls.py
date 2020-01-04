from django.urls import path
from .views import HomePageView
from .views import TestPageView
from .views import AgainPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('test/', TestPageView.as_view(), name='test'),
    path('again/', AgainPageView.as_view(), name='again')
]