from django.contrib import admin

from recipes.models import (Tag, Recipe, Ingredient, 
                            RecipeIngredient, Shopping_cart, Favorite)
from users.models import Follow


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'favorites_count')
    inlines = (RecipeIngredientInLine,)
    list_filter = ('name', 'author', 'tags')

    def favorites_count(self, obj):
        return obj.favorite.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('name',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass

@admin.register(Shopping_cart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass