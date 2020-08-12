from django.urls import path

from portfolio.views import home, blog, readingList, portfolio

urlpatterns = [
    path('', home, name="home"),
    path('blog/', blog, name="blog"),
    path('portfolio/', portfolio, name="portfolio"),
    path('readinglist/', readingList, name="readingList"),
    
]

