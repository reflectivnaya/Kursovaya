from django.contrib import admin
from .models import Author
from reviews.models import Review

class ReviewInline(admin.TabularInline):
    model = Review
    fields = ('title', 'description')

class AuthorAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ('name', 'surname', 'phone')

admin.site.register(Author)