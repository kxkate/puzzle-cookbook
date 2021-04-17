from django.core.management.base import BaseCommand, CommandError
from cookbook.models import Ingredient
import csv


class Command(BaseCommand):
    help = 'Downloads ingredient data from top-1k-ingredients database'

    def handle(self, *args, **options):
        with open('cookbook/static/cookbook/top-1k-ingredients.csv','r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for idx, row in enumerate(reader):
                Ingredient.objects.create(ingredient_name=row[0])


