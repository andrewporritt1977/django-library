from django.urls import path
from django.conf.urls import url, include
from .views import HomePageView, logout, login, signup, user_card
from library_app import url_reset

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('logout/' , logout, name='logout'),
    path('login/' , login , name='login'),
    path('signup/' , signup, name='signup'),
    path('card/', user_card , name='user_card'),
    url('password-reset/', include(url_reset))
]