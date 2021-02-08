from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=150)
    creation_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/blog")
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        sum_words = 20
        summarized = self.body.split(" ")
        return " ".join(summarized[:sum_words]) + "..."

    def pretty_date(self):
        return self.creation_date.strftime("%b %e %Y")
