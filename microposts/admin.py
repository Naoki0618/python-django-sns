from django.contrib import admin
from .models import Post, Message, Favorite


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["owner", "content", "created_at"]


@admin.register(Message)
class UserAdmin(admin.ModelAdmin):
    model = Message
    list_display = ["id", "post_id", "user_name", "comment", "created_at"]


@admin.register(Favorite)
class UserAdmin(admin.ModelAdmin):
    model = Favorite
    list_display = ["user_name", "post_id", "created_at"]

    def __str__(self):
        return str(self.post_id)
