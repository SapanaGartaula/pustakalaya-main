from django.shortcuts import render, redirect

from . import models
from django.db.models import Q

# Create your views here.
def index(request):
    book = models.Book.objects.filter(is_available=True)
    context = {
        'user' : request.user,
        'book' : book,  
    }
    return render(request,'index.html',context)


def book_detail(request, book_slug):
    book = models.Book.objects.filter(slug=book_slug)[0]
    context = {
        "book":book,
    }
    return render(request, 'bookdetails.html', context)


def search(request):
    book = None
    keyword = None
    if 'keyword' in request.GET:
        print(keyword)
        keyword = request.GET['keyword']
        if keyword:
            book = models.Book.objects.filter(Q(book_name__icontains=keyword) | Q(author__icontains=keyword)  |Q(description__icontains=keyword))
            context ={
                'book': book,
            }
        else:
            pass
    return render(request, 'search.html', context)

def terms(request):
    return render(request, 'terms.html')
def about(request):
    return render(request, 'about.html')
