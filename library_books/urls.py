from django.conf.urls import url, include
from .views import all_books, check_out, add_book, archive_book, edit_book, delete_book


urlpatterns = [
    url(r'^$', all_books, name='books'),
    url(r'^add/$', add_book, name="add_book"),
    url(r'^(?P<pk>\d+)edit/$', edit_book, name="edit_book"),
    url(r'^(?P<pk>\d+)delete/$', delete_book, name="delete_book"),
    url(r'^(?P<pk>\d+)/$', check_out, name='check_out'),
    url(r'^(?P<pk>\d+)$', archive_book, name='archive_book')
    
]
