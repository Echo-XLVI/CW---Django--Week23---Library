from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.

class TestAllBooks(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Book.objects.create(title = 'بوستان', author = 'سعدی',ISBN = 10203040, published_date = '1990-06-06', available = True)
        Book.objects.create(title = 'گلستان', author = 'سعدی',ISBN = 10203040, published_date = '1990-06-06', available = True)
        cls.books = Book.objects.all()

    def test_first_book(self):
        self.assertEqual(self.books[0].title, 'بوستان')
        self.assertEqual(self.books[0].author, 'سعدی')
        self.assertEqual(self.books[0].ISBN, 10203040)
        self.assertEqual(self.books[0].published_date.year , 1990)


    def test_url_exist(self):
        response = self.client.get('/all_books/')
        self.assertEqual(response.status_code, 200) 

    def test_url_exist_by_name(self):
        response = self.client.get(reverse('all_books'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse('all_books'))
        self.assertTemplateUsed(response, 'all_books.html')