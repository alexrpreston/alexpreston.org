from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "portfolio/home.html")

def portfolio(request):
    return render(request, "portfolio/portfolio.html")

def blog(request):
    return render(request, "portfolio/blog.html")

def readingList(request):
    return render(request, "portfolio/readingList.html")