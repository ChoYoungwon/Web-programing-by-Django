from django.contrib import admin
from .models import bookmark

@admin.register(bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

