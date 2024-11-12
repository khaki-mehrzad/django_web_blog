from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogSpot(models.Model):
    title = models.CharField(max_length=100)
    text  = models.TextField()
    owner = models.ForeignKey(User, models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}  :: {self.text}"
    