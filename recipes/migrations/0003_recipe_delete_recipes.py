# Generated by Django 4.2.7 on 2023-11-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_recipe_recipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cooking_time', models.IntegerField(help_text='in minutes')),
                ('ingredients', models.CharField(max_length=400)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Recipes',
        ),
    ]
