from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def index(request):
    feature1 = Feature()
    feature1.name = 'STYLISH SHOES'
    feature1.subname = 'Nike, addidas, NewBalance'
    feature1.description = 'We deal with the best brands when it comes to shoes...'

    feature2 = Feature()
    feature2.name = 'Hair Treatment'
    feature2.subname = 'Lux, Apple, Nivea, SoftGel'
    feature2.description = 'Are you tired of searching different stores trying to find the perfect hair treatment for your hair. Then look no further because we have got the best treatment for you that will give your hair that glamous look and feel.'
    
    feature3 = Feature()
    feature3.name = 'Garden Kits'
    feature3.subname = 'GreenFarm, Famers Kit, RedRose'
    feature3.description = 'There are alot of gardening kit that would give your garden that relaxing look and feel.'

    
    return render(request, 'index.html', {'feature': feature1, 'features': feature2, 'feature3': feature3})

def home(request):
    return render(request, 'shop.html')

def shop(request):
    return render(request, 'shop-single.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request , 'contact.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
