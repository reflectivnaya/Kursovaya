from django.contrib import admin
from reviews.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('author',)

admin.site.register(Review, ReviewAdmin)

