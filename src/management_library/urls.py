from django.urls import path
from .views import all_books,detail_single_book,all_members,detail_single_member

urlpatterns = [
    path('all_books/',all_books , name='all_books'),
    path('all_member/',all_members ),
    path('detail_book/<pk>',detail_single_book,name='detail_book'),
    path('detail_member/<pk>',detail_single_member,name='detail_member'),
]
