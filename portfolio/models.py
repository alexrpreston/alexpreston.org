from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, default=0)
    notes = MarkdownxField(default=0)
    favorite = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = MarkdownxField()
    created_on = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title