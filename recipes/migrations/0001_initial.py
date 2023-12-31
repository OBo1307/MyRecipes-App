# Generated by Django 4.2.7 on 2023-11-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]
