from django.db import models


class Product(models.Model):
    """
    Модель продукта, содержащая информацию о названии, описании и цене
    продукта.
    """

    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", '-price']

    def __str__(self):
        return self.name
