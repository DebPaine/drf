from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(
        blank=True, null=True
    )  # blank=True is to allow empty value in form, null=True is to enter null value in DB if it's empty in form
    price = models.DecimalField(max_digits=15, decimal_places=2, default=100.0)

    @property
    def sale_price(self):
        return f"{float(self.price)*0.6:.2f}"

    def discount(self):
        return 0.8

    def __str__(self) -> str:
        return self.title
