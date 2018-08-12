from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'date_added']

    class Meta:
        model = Comment


admin.site.register(Comment)
