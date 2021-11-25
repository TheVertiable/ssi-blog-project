
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):  # class name is given whatever table name we want
    STATUS_CHOICEs = (           
        ("draft", "Draft"),
        ("published", "Published",)
    )
    title = models.CharField(
        max_length=225
    )  # whatever the name you are giving it will creat a coloumn in table
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    content = models.TextField()
    published_at = models.DateTimeField(default = timezone.now)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICEs)

    class Meta:
        ordering = ("-published_at",)  #tuple

    def __str__(self):
        #return self.title
        return f"{str(self.id)}-{self.title}"
        #return str(self.id)+self.title


