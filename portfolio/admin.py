from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_display = ('year')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book)
admin.site.register(Post, MarkdownxModelAdmin)