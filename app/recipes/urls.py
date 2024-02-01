from django.urls import path

from .views import add_product, cook_recipe, recipes_list, show_recipes_without_product

urlpatterns = [
    path("", recipes_list, name="recipes"),
    path(
        "add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/",
        add_product,
        name="add_product",
    ),
    path("cook_recipe/<int:recipe_id>/", cook_recipe, name="cook_recipe"),
    path(
        "show_recipes_without_product/<int:product_id>/",
        show_recipes_without_product,
        name="show_recipes_without_product",
    ),
]
