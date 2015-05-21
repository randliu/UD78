from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Stock

def list_stock():
    
    lst_stock = Stock.objects.all()
    
    return HttpResponse(str(lst_stock))
    
    pass