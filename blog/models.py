from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=150)
    creation_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/blog")
    body = models.TextField()
