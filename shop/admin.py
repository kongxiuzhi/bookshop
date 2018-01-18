from django.contrib import admin
from .models import Book,Category
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display =['title','author','pubdate','price','stock','sale']
	list_filter = ['author','pubdate']
	list_editable = ['price','stock','sale']
	search_fields = ['author','title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']
















