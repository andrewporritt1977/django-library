from django.urls import path
from .views import HomePageView, LoginPageView, LibraryPageView, logout

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('library_view/', LibraryPageView.as_view(), name='library_view'),
    path('logout/' , logout, name='logout')
]