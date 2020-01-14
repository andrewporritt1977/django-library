from django.conf.urls import url, include
from .views import all_books, check_out


urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^$', check_out, name='check_out')
]
