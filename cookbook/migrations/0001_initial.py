# Generated by Django 3.1.7 on 2021-04-06 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=128)),
                ('dish_type', models.CharField(max_length=10)),
                ('cuisine_type', models.CharField(max_length=128)),
                ('preparation_time', models.IntegerField()),
                ('servings_number', models.IntegerField()),
                ('description', models.TextField()),
                ('user_profiles', models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
                ('kcal_value_100g', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodRecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
                ('ingredient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cookbook.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='cookbook.foodrecipe')),
            ],
        ),
    ]
