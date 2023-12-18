from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns =[
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('book/<slug:book_slug>/', views.book_detail, name='book_detail'),
    path('terms', views.terms, name='terms'),
    path('about', views.about, name='about'),
]