from django.conf.urls import url
from .views import book_search, genre_filter, reset_view

urlpatterns = [
    url(r'^$', book_search, name='search'),
    url(r'^filt$', genre_filter, name='filter'),
    url(r'^reset$', reset_view, name='reset_view')
]
