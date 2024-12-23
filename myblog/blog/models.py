from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to='', default='default.png', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
