from django.contrib import admin
<<<<<<< HEAD
from .models import Category, Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

=======

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...


>>>>>>> c976c6b (Aula_62)
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

<<<<<<< HEAD
admin.site.register(Category, CategoryAdmin)
=======

admin.site.register(Category, CategoryAdmin)
>>>>>>> c976c6b (Aula_62)
