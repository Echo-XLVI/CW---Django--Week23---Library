from django.shortcuts import render
from .models import Book,Member
# Create your views here.


def all_books(request):
  books = Book.objects.all()
  return render(request, 'all_books.html', {'books':books})

def detail_single_book(request,pk):
  book = Book.objects.get(pk=pk)
  return render(request, 'detail_single_book.html',{'books':book})

def all_members(request):
  members = Member.objects.all()
  return render(request, 'all_member.html', {'members':members})

def detail_single_member(request,pk):
  member = Member.objects.get(pk=pk)
  return render(request, 'detail_single_member.html',{'members':member})
