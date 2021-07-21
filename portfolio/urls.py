from django.urls import path

from portfolio.views import home, blog, portfolio, resume, PostDetail, PostList, BookList, BookDetail

urlpatterns = [
    path('', home, name="home"),
    path('portfolio/', portfolio, name="portfolio"),
    path('resume/', resume, name="resume"),
    path('blog/', PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('bookshelf/', BookList.as_view(), name='bookList'),
    path('bookshelf/<slug:slug>/', BookDetail.as_view(), name='bookNotes'),
    
]

