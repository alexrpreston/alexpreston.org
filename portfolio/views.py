from django.shortcuts import render
from django.views import generic
from .models import Post, Book
# Create your views here.
from django import template
from markdownx.utils import markdownify

register = template.Library()

def home(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'post_list': queryset
    }
    return render(request, "portfolio/home.html", context)

def portfolio(request):
    return render(request, "portfolio/portfolio.html")

def blog(request):
    return render(request, "portfolio/blog.html")

def readingList(request):
    bookInfo = Book.objects.all()[0:]
    context = {
        'book_Info' : bookInfo
    }
    return render(request, "portfolio/readingList.html", context)

def resume(request):
    return render(request, "portfolio/resume.html")

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'portfolio/blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'portfolio/post_detail.html'