from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Product, Recipe, Weight


class WeightInlineFormset(BaseInlineFormSet):
    def clean(self):
        products = []
        for form in self.forms:
            product = form.cleaned_data.get("product")
            print(product)
            weight = form.cleaned_data.get("weight")
            if product in products:
                raise ValidationError("Каждый продукт можно добавить только 1 раз")
            if product and weight == 0:
                raise ValidationError("Укажите вес продукта")

            products.append(product)
        return super().clean()


class WeightInline(admin.TabularInline):
    model = Weight
    formset = WeightInlineFormset
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    inlines = [WeightInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "dishes_count")
