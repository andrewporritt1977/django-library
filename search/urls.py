from django.conf.urls import url
from .views import book_search, genre_filter

urlpatterns = [
    url(r'^$', book_search, name='search'),
    url(r'^filt$', genre_filter, name='filter')

]
