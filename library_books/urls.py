from django.conf.urls import url, include
from .views import all_books


urlpatterns = [
    url(r'^$', all_books, name='books'),
]
