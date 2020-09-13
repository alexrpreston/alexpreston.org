from django.urls import path

from portfolio.views import home, blog, readingList, portfolio, resume, PostDetail, PostList

urlpatterns = [
    path('', home, name="home"),
    path('portfolio/', portfolio, name="portfolio"),
    path('readinglist/', readingList, name="readingList"),
    path('resume/', resume, name="resume"),
    path('blog/', PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]

