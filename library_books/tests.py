from django.test import TestCase
from .models import Book
# Create your tests here.

class BookTests(TestCase):

    def test_str(self):
        test_name = Book(title="A Book")
        self. assertEqual(str(test_name), 'A Book')

    def function_test(self):
        