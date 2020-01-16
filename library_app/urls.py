from django.urls import path, reverse_lazy
from django.conf.urls import url, include
from .views import HomePageView, logout, login, signup, user_card
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .views import password_reset_complete, password_reset_done, pay

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('logout/' , logout, name='logout'),
    path('login/' , login , name='login'),
    path('signup/' , signup, name='signup'),
    path('card/', user_card , name='user_card'),
    path('pay/', pay, name='pay'),
    url(r'^password_reset/$', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done , name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view()
       , {'post_reset_confirm' : reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete , name='password_reset_complete')
]