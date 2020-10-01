from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = MarkdownxField()
    created_on = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def formatted_markdown(self):
            return markdownify(self.body)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title