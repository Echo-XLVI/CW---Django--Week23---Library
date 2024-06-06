from django.shortcuts import render
from .models import Book
# Create your views here.


def all_books(request):
  books = Book.objects.all()
  print(books)
  return render(request, 'all_books.html', {'books':books})

def detail_single_book(request,pk):
    


