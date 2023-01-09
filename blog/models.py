from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published", "Published"),
)


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    excerpt = models.CharField(null=True, blank=True, max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    objects = models.Manager()  # The default manager.
    postobjects = PostObjects()  # Our custom manager.

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title
