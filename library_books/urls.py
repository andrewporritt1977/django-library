from django.conf.urls import url, include
from .views import all_books, check_out, add_book


urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^add/$', add_book, name="add_book"),
    url(r'^(?P<pk>\d+)/$', check_out, name='check_out')
]
