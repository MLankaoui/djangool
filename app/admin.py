from django.contrib import admin
from app.models import Posts

# Register your models here.
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
