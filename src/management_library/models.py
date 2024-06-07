from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    ISBN = models.IntegerField()
    available = models.BooleanField()

    def title_author(self):
        return f"{self.title} by {self.author}"

    def __str__(self):
        return f"{self.title} {self.author}"

class Member(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    membership_date = models.DateField()

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date =models.DateField(auto_now_add=True) 
    return_date = models.DateField(auto_now_add=True)