from django.conf.urls import url
from .views import book_search

urlpatterns = [
    url(r'^$', book_search, name='search')
]
