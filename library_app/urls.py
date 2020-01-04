from django.urls import path
from .views import HomePageView, LibraryPageView, logout, login, signup

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('library_view/', LibraryPageView.as_view(), name='library_view'),
    path('logout/' , logout, name='logout'),
    path('login/' , login , name='login'),
    path('signup/' , signup, name='signup')
]