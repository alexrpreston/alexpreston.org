from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.
from django import template
from markdownx.utils import markdownify

register = template.Library()

def home(request):
    return render(request, "portfolio/home.html")

def portfolio(request):
    return render(request, "portfolio/portfolio.html")

def blog(request):
    return render(request, "portfolio/blog.html")

def readingList(request):
    return render(request, "portfolio/readingList.html")

def resume(request):
    return render(request, "portfolio/resume.html")

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'portfolio/blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'portfolio/post_detail.html'