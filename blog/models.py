import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=255, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
