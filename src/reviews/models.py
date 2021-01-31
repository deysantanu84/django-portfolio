from django.db import models
from django.urls import reverse


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("reviews:review-detail", kwargs={"id": self.id})
