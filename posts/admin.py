from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['title', 'created_at', 'updated_at']