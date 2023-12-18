from django.db import models

from accounts.models import Account
from home.models import Book

# Create your models here.

class Cart(models.Model):
    card_id = models.CharField(max_length=300, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.card_id
    

class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product
    
    def total(self):
        return self.quantity * self.book.price
    