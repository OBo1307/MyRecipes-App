from django.urls import path
from .views import home
from .views import RecipeListView
from .views import RecipeDetailView
from .views import records
from .views import add_recipe

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('search/', records, name='search'),
    path('add/', add_recipe, name='add'),
]
