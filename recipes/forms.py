from django import forms
from .models import Recipe

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(
        label="Recipe Name",
        max_length=100,
        required=False,
    )
    ingredients = forms.CharField(
        label="Ingredients (separated by commas)",
        max_length=100,
        required=False,
    )
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cooking_time', 'ingredients', 'description', 'pic']