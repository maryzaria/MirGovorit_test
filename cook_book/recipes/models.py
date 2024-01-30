from django.db import models


class Product(models.Model):
    title = models.CharField(
        max_length=100, unique=True, verbose_name="Название продукта"
    )
    dishes_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество рецептов"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["id"]

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название рецепта", unique=True
    )
    products = models.ManyToManyField(Product, related_name="recipes", through="Weight")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ["id"]

    def __str__(self):
        return self.title


class Weight(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="weight"
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="weight")
    weight = models.PositiveIntegerField(default=0, verbose_name="Вес")

    class Meta:
        verbose_name = "Вес продукта"

    def __str__(self):
        return f"{self.product} - {self.weight}"
