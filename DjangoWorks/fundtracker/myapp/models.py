from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Expense(models.Model):

    title = models.CharField(max_length=200)

    amount = models.PositiveIntegerField()

    EXPENSE_CATEGORIES = (
            ('Housing', 'Housing'),
            ('Transportation', 'Transportation'),
            ('Food', 'Food'),
            ('Healthcare', 'Healthcare'),
            ('Education', 'Education'),
            ('Entertainment', 'Entertainment'),
            ('Personal Care', 'Personal Care'),
            ('Debt Payments', 'Debt Payments'),
            ('Savings & Investments', 'Savings & Investments'),
            ('Gifts & Donations', 'Gifts & Donations'),
            ('Insurance', 'Insurance'),
            ('Travel', 'Travel'),
            ('Miscellaneous', 'Miscellaneous'),
        )
    
    category = models.CharField(max_length=100,choices=EXPENSE_CATEGORIES,default="Miscellaneous")

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        
        return self.title

