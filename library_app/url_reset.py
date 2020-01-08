from django.conf.urls import url
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', auth_views.password_reset, name='password_reset'),
    url(r'^done/$', auth_view.password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,
        {'post_reset_confirm' : reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^complete/$', auth_views.password_reset_complete , name='password_reset_complete')
]