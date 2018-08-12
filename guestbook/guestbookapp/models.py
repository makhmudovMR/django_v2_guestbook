from django.db import models
from django.utils import timezone


class Comment(models.Model):

    name = models.CharField(max_length=50)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    class Meta:

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'