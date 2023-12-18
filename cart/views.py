from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from home import models
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItem
from django.contrib import messages

from home.models import Book


def _cart_id(request):
    cart = request.session.session_key
    
    if not cart:
        cart = request.session.create()
    return cart

@login_required
def add_to_cart(request, book_id):
    user = request.user
    book = models.Book.objects.get(id=book_id)
    if user.is_authenticated:
        try:
            cart = Cart.objects.get(card_id=_cart_id(request))
        except Cart.DoesNotExist:
            #create a new cart
            cart = Cart.objects.create(
                card_id = _cart_id(request)
            )
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(book=book, user=user).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(book=book, user=user)[0]
            cart_item.quantity +=1
            cart_item.save()
            
        else:
            cart_item = CartItem.objects.create(book=book, cart=cart, quantity=1, user=user)
            cart_item.save()
        return redirect('cart')
    else:
        messages.error(request, "You need to be logged to add to the cart!")
        return redirect("login")


@login_required
def cart(request):
    current_user = request.user
    total = 0
    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(user=current_user, is_active=True)

    for book in cart_item:
        total += (book.book.price * book.quantity)
    grand_total= total + 100
    context = {
        "cart_item":cart_item,
        "total" : total,
        "grand_total" : grand_total
    }
    return render(request,'cart.html', context)


def remove_cart_book(request, book_id, cart_item_id):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, id=book_id)
        cart_item = CartItem.objects.get(book=book, user=request.user, id=cart_item_id)
        cart_item.delete()
        return redirect('cart')
    
def decrement_cart_item(request, book_id, cart_item_id):
    current_user = request.user
    if current_user.is_authenticated:
        book = get_object_or_404(Book, id=book_id)
        cart_item = CartItem.objects.get(book=book, user=current_user, id=cart_item_id)

        print(cart_item)
        if cart_item.quantity > 1 :
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete() # delete if item is only one
        return redirect('cart')
    
def increment_cart_item(request, book_id, cart_item_id):
    current_user = request.user
    if current_user.is_authenticated:
        book = get_object_or_404(Book, id=book_id)
        cart_item = CartItem.objects.get(book=book, user=current_user, id=cart_item_id)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart')
    

def checkout(request):
    total = 0
    user = request.user
    cart_item = CartItem.objects.filter(user=user)

    no_item = cart_item.count()
    for book in cart_item:
        total += (book.book.price * book.quantity)
    grand_total= total + 100

    context = {
        'cart':cart,
        'no_item':no_item,
        'grand_total':grand_total,
    }
    return render(request, 'form.html',context)

def payment(request):
    user = request.user
    
    return render(request, 'payment.html')