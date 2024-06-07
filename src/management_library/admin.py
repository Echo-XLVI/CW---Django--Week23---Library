from django.contrib import admin
from .models import Book , Member ,Loan
# Register your models here.
# admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Loan)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title_author","published_date",'available']
    ordering = ('title',)
    # for filtering 
    list_filter = ['published_date' , "available"]
    # for searching 
    search_fields = ["title"]