from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Stock

@login_required
def home(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/home.html', {'stocks': stocks})
