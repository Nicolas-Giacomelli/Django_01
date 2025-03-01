from django.urls import path
<<<<<<< HEAD
=======

>>>>>>> c976c6b (Aula_62)
from . import views

app_name = 'recipes'

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]
=======
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
>>>>>>> c976c6b (Aula_62)
