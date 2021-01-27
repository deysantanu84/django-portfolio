from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length=required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(blank=True, null=False)  # default=
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f"{self.id}/"
        # return reverse("products:product-detail", kwargs={"id": self.id})
