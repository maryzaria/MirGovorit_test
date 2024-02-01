from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from recipes.models import Product, Recipe, Weight


def recipes_list(request):
    recipes = Recipe.objects.all().order_by("title")

    paginator = Paginator(recipes, 3)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, template_name="recipes.html", context=context)


def add_product(request, recipe_id, product_id, weight):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        product = Product.objects.get(id=product_id)
        Weight.objects.update_or_create(
            product=product, recipe=recipe, defaults={"weight": weight}
        )
        ingredients = ", ".join(
            [f"{item.product} - {item.weight} г" for item in recipe.weight.all()]
        )
        return HttpResponse(f"Рецепт: {recipe}, состав: {ingredients}")
    except Recipe.DoesNotExist:
        return HttpResponse("Рецепт не найден")
    except Product.DoesNotExist:
        return HttpResponse("Продукт не найден")
    except Exception:
        return HttpResponse("Непредвиденная ошибка")


def cook_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        for item in recipe.weight.all():
            item.product.dishes_count += 1
            item.product.save()
        return HttpResponse("Изменения внесены: количество блюд увеличено")
    except Recipe.DoesNotExist:
        return HttpResponse("Рецепт не найден")
    except Exception:
        return HttpResponse("Непредвиденная ошибка")


def show_recipes_without_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        recipes1 = Recipe.objects.exclude(weight__product=product)
        recipes2 = Recipe.objects.filter(
            weight__product=product, weight__weight__lte=10
        )
        recipes = list(set(recipes1 | recipes2))
        paginator = Paginator(recipes, 3)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        context = {"page_obj": page_obj, "product": str(product)}
        return render(
            request, template_name="recipes_without_product.html", context=context
        )
    except Product.DoesNotExist:
        return HttpResponse("Продукт не найден")
    except Exception as e:
        return HttpResponse(f"Непредвиденная ошибка {e}")
