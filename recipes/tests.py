from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm
# Create your tests here.

class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(
            name='Test Recipe',
            cooking_time=15,
            ingredients='Ingredient 1, Ingredient 2, Ingredient 3',
            description='Test recipe description'
        )

    def test_recipe_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_calculate_difficulty_easy(self):
        recipe = Recipe.objects.get(id=1)
        recipe.cooking_time = 5
        recipe.ingredients = 'Ingredient 1, Ingredient 2'
        expected_difficulty = 'Easy'
        self.assertEqual(recipe.calculate_difficulty(), expected_difficulty)
    
    def test_calculate_difficulty_medium(self):
        recipe = Recipe.objects.get(id=1)
        recipe.cooking_time = 5
        recipe.ingredients = 'Ingredient 1, Ingredient 2, Ingredient 3, Ingredient 4, Ingredient 5, Ingredient 6, Ingredient 7'
        expected_difficulty = 'Medium'
        self.assertEqual(recipe.calculate_difficulty(), expected_difficulty)

    def test_calculate_difficulty_intermediate(self):
        recipe = Recipe.objects.get(id=1)
        recipe.cooking_time = 15
        recipe.ingredients = 'Ingredient 1, Ingredient 2'
        expected_difficulty = 'Intermediate'
        self.assertEqual(recipe.calculate_difficulty(), expected_difficulty)

    def test_calculate_difficulty_hard(self):
        recipe = Recipe.objects.get(id=1)
        recipe.cooking_time = 15
        recipe.ingredients = 'Ingredient 1, Ingredient 2, Ingredient 3, Ingredient 4, Ingredient 5, Ingredient 6, Ingredient 7'
        expected_difficulty = 'Hard'
        self.assertEqual(recipe.calculate_difficulty(), expected_difficulty)

class RecipeFormTest(TestCase):
    def test_recipe_form_valid_data(self):
        form_data = {
            'recipe_name': 'Test Recipe',
            'ingredients': 'Ingredient 1, Ingredient 2, Ingredient 3',
            'chart_type': '#1'
        }
        form = RecipesSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_form_invalid_data(self):
        form_data = {
            'recipe_name': 'Test Recipe' * 100,  # Exceeds max length
            'ingredients': 'Ingredient 1, Ingredient 2, Ingredient 3' * 100,  # Exceeds max length
            'chart_type': '#4'  # Invalid choice
        }
        form = RecipesSearchForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Three fields should have errors
