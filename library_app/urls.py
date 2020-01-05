from django.urls import path
from django.conf.urls import url, include
from .views import HomePageView, LibraryPageView, logout, login, signup, user_card
import url_reset

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('library_view/', LibraryPageView.as_view(), name='library_view'),
    path('logout/' , logout, name='logout'),
    path('login/' , login , name='login'),
    path('signup/' , signup, name='signup'),
    path('card/', user_card , name='user_card'),
    url('password-reset/', include(url_reset))
]