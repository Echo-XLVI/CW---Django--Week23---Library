from django.contrib import admin
from django.urls import path,include
from .views import all_books,detail_single_book
urlpatterns = [
    path('all_books',all_books ),
    path('detail_book/<pk>',detail_single_book,name='detail_book')
]
